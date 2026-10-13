"""Judge a finished trainee (stats, aptitudes, skills) against the guide docs. Pure and stdlib-only.

Every number here comes from AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md (section noted per check) or from the
skill tables in Skill/skill.md. No model writes any verdict: the model only transcribes the screenshot, this module
does the maths and produces findings with the reason and source for each. Where the docs give a range or nothing at
all, the result says so instead of picking a number.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass, field

from .TraineeSheet import DISTANCES, GRADES, STATS, STYLES, SURFACES, Sheet, SkillRead
from .UmamusumeSkills import SkillCatalog, default_catalog

HEAL_GOLD, HEAL_WHITE = 5.5, 1.5  # % of max HP per recovery skill (Part 2 s2.4, S3)
DEFAULT_CAP = 1600

DISTANCE_LABEL = {"sprint": "Sprint", "mile": "Mile", "medium": "Medium", "long": "Long"}
STYLE_LABEL = {"front": "Front Runner", "pace": "Pace Chaser", "late": "Late Surger", "end": "End Closer"}
SURFACE_LABEL = {"turf": "Turf", "dirt": "Dirt"}

# Aptitude modifiers, Part 2 s2.2. Distance -> speed, surface -> acceleration, style -> Wit.
_DISTANCE_MOD = dict(zip(GRADES, ("+5%", "0%", "-10%", "-20%", "-40%", "-60%", "-80%", "-90%")))
_SURFACE_MOD = dict(zip(GRADES, ("+5%", "0%", "-10%", "-20%", "-30%", "-50%", "-70%", "-90%")))
_STYLE_MOD = dict(zip(GRADES, ("+10%", "0%", "-15%", "-25%", "-40%", "-60%", "-80%", "-90%")))


# --------------------------------------------------------------------------- formulas


def base_stat(raw: int) -> float:
    """Raw stat above 1200 is halved before it becomes the base stat (Part 2 s2.1). Mood is unknown, so 1.00."""
    return float(raw) if raw <= 1200 else 1200 + (raw - 1200) / 2


def skill_activation_pct(wit_base: float) -> float:
    """max(100 - 9000/Wit, 20)% (Part 2 s2.3)."""
    return max(100 - 9000 / wit_base, 20.0) if wit_base > 0 else 20.0


def rushed_pct(wit_base: float) -> int:
    """(6.5 / log10(0.1*Wit + 1))^2 %, rounded up to the next whole percent (Part 2 s2.9)."""
    return math.ceil((6.5 / math.log10(0.1 * wit_base + 1)) ** 2)


# Stamina vs Guts (Part 2 s2.4, ottoh via S3). Each distance has a target Guts; above it Guts is worth less than
# Stamina point for point, below it more. Values are Stamina-equivalents.
_ABOVE = ((50, 43, 46), (50, 33, 37), (50, 30, 31))  # (width, low, high) for each successive 50 above the target
_BELOW = ((0, 0, 0), (50, 55, 62), (100, 66, 83), (150, 82, 106))  # cumulative cost of being this far below


def _above(surplus: float) -> tuple[float, float]:
    lo = hi = 0.0
    left = surplus
    for width, a, b in _ABOVE:
        take = min(left, width)
        lo += a * take / width
        hi += b * take / width
        left -= take
        if left <= 0:
            return lo, hi
    # Past the last tier the guide gives nothing: the low estimate adds no more, the high one keeps the last rate.
    return lo, hi + 31 * left / 50


def _below(deficit: float) -> tuple[float, float]:
    if deficit >= 150:
        extra = deficit - 150  # the last tier adds 16-23 per 50
        return 82 + 16 * extra / 50, 106 + 23 * extra / 50
    for (d0, l0, h0), (d1, l1, h1) in zip(_BELOW, _BELOW[1:]):
        if deficit <= d1:
            f = (deficit - d0) / (d1 - d0)
            return l0 + (l1 - l0) * f, h0 + (h1 - h0) * f
    return 0.0, 0.0


def _guts_value(guts: float, threshold: float) -> tuple[float, float]:
    if guts >= threshold:
        return _above(guts - threshold)
    lo, hi = _below(threshold - guts)
    return -hi, -lo


def guts_adjustment(guts: float, baseline: float, threshold: float) -> tuple[float, float]:
    """Stamina-equivalent of having `guts` instead of the `baseline` Guts the required-Stamina table assumes."""
    g_lo, g_hi = _guts_value(guts, threshold)
    b_lo, b_hi = _guts_value(baseline, threshold)
    # Same end of the guide's range at both points, so having exactly the baseline Guts adjusts by exactly zero.
    return g_lo - b_lo, g_hi - b_hi


@dataclass(frozen=True)
class Course:
    key: str
    label: str
    distance: str
    baseline_guts: int  # Guts the table assumes: 300 Sprint/Mile, 400 Medium/Long
    threshold_guts: int  # the guide's per-distance target Guts
    rows: tuple[tuple[int, tuple[int, int, int, int]], ...]  # (gold recoveries, Front/Pace/Late/End Stamina)


# Required Stamina, Part 2 s2.4 (S3 with Umalator): 1200 Speed/Power, 600 Wit, no downhills.
COURSES = (
    Course("sprint", "Short 1400m", "sprint", 300, 210, ((0, (570, 540, 500, 510)),)),
    Course("mile", "Mile 1800m", "mile", 300, 260, ((0, (800, 770, 720, 740)), (1, (640, 600, 560, 580)))),
    Course("medium", "Mid 2400m", "medium", 400, 320, ((1, (910, 930, 870, 900)), (2, (710, 720, 680, 700)))),
    Course("long2600", "Long 2600m", "long", 400, 380, ((1, (1130, 1110, 1030, 1060)), (2, (900, 870, 820, 850)))),
    Course("long3200", "Long 3200m", "long", 400, 380, ((2, (1080, 1060, 990, 1020)), (3, (830, 800, 750, 780)))),
)


def required_stamina(course: Course, style: str, gold_eq: float) -> tuple[float, bool]:
    """Table value for `gold_eq` gold-recovery equivalents, linear between rows. Second value: extrapolated."""
    idx = STYLES.index(style)
    pts = [(g, vals[idx]) for g, vals in course.rows]
    if len(pts) == 1:
        return float(pts[0][1]), False
    if gold_eq <= pts[0][0]:
        (g0, n0), (g1, n1) = pts[0], pts[1]
    elif gold_eq >= pts[-1][0]:
        (g0, n0), (g1, n1) = pts[-2], pts[-1]
    else:
        (g0, n0), (g1, n1) = next((a, b) for a, b in zip(pts, pts[1:]) if a[0] <= gold_eq <= b[0])
    need = n0 + (n1 - n0) * (gold_eq - g0) / (g1 - g0)
    extrapolated = gold_eq < pts[0][0] or gold_eq > pts[-1][0]
    return max(need, 0.5 * min(n for _, n in pts)), extrapolated


# --------------------------------------------------------------------------- what the user asked for


@dataclass(frozen=True)
class Goal:
    distances: tuple[str, ...] = ()
    styles: tuple[str, ...] = ()
    surface: str | None = None


@dataclass(frozen=True)
class Target:
    surface: str | None
    distance: str
    style: str

    @property
    def label(self) -> str:
        surface = f" on {SURFACE_LABEL[self.surface]}" if self.surface else ""
        return f"{DISTANCE_LABEL[self.distance]} {STYLE_LABEL[self.style]}{surface}"


_DISTANCE_RE = re.compile(r"\b(sprint|short|mile|medium|mid|long)\b", re.I)
_STYLE_RE = re.compile(r"\b(front(?:\s+runner)?|runner|nige|pace(?:\s+chaser)?|late(?:\s+surger)?|end\s+closer|closer)\b", re.I)
_SURFACE_RE = re.compile(r"\b(turf|dirt)\b", re.I)
_CAP_RE = re.compile(r"\b(\d{4})\s*(?:stat\s*)?cap\b|\bcap\s*(?:of|is|=|:)?\s*(\d{4})\b", re.I)
_DISTANCE_WORD = {"short": "sprint", "mid": "medium"}


def parse_goal(text: str) -> tuple[Goal, int | None]:
    """Pull a target (distance, style, surface) and a stat cap out of the user's caption. All optional."""
    text = text or ""
    distances = tuple(dict.fromkeys(_DISTANCE_WORD.get(w.lower(), w.lower()) for w in _DISTANCE_RE.findall(text)))
    styles: list[str] = []
    for w in _STYLE_RE.findall(text):
        w = w.lower().split()[0]
        styles.append({"front": "front", "runner": "front", "nige": "front", "pace": "pace", "late": "late",
                       "end": "end", "closer": "end"}[w])
    surface = None
    m = _SURFACE_RE.search(text)
    if m:
        surface = m.group(1).lower()
    cap = None
    m = _CAP_RE.search(text)
    if m:
        value = int(m.group(1) or m.group(2))
        if 1000 <= value <= 3000:
            cap = value
    return Goal(distances, tuple(dict.fromkeys(styles)), surface), cap


MAX_TARGETS = 6


def pick_targets(sheet: Sheet, goal: Goal) -> tuple[list[Target], list[str]]:
    """The targets to judge. Asked-for ones as given; otherwise every distance/style she has at A or better."""
    notes: list[str] = []
    apt = sheet.aptitudes

    def good_keys(keys: tuple[str, ...]) -> list[str]:
        known = {k: apt[k] for k in keys if k in apt}
        if not known:
            return list(keys)
        top = [k for k in keys if k in known and GRADES.index(known[k]) <= 1]
        if top:
            return top
        best = min(known.values(), key=GRADES.index)
        return [k for k in keys if known.get(k) == best]

    distances = list(goal.distances) or good_keys(DISTANCES)
    styles = list(goal.styles) or good_keys(STYLES)
    surface = goal.surface
    if surface is None:
        known = {k: apt[k] for k in SURFACES if k in apt}
        surface = min(known, key=lambda k: (GRADES.index(known[k]), SURFACES.index(k))) if known else None
    targets = [Target(surface, d, s) for d in distances for s in styles]
    if len(targets) > MAX_TARGETS:
        notes.append(f"Judged the first {MAX_TARGETS} of {len(targets)} possible targets; say which distance/style you want for the rest.")
        targets = targets[:MAX_TARGETS]
    return targets, notes


# --------------------------------------------------------------------------- skills


@dataclass
class ResolvedSkill:
    name: str
    tier: str  # unique | rare | normal | negative
    kind: str
    scope: tuple[str, ...]
    known: bool  # found in the skill docs
    heal_pct: float = 0.0
    own_unique: bool = False
    inherited_unique: bool = False


_ICON_KIND = {"recovery": "Recovery", "speed": "Velocity", "acceleration": "Acceleration", "green": "Green Skill",
              "debuff": "Debuff", "other": "Speed - Other"}
_RARITY_TIER = {"gold": "rare", "white": "normal", "unique": "unique", "negative": "negative"}


def _is_own_unique(owner: str, sheet: Sheet) -> bool:
    low = owner.lower()
    if not sheet.trainee or sheet.trainee.lower() not in low:
        return False
    return not sheet.outfit or sheet.outfit.lower() in low


def resolve_skill(read: SkillRead, catalog: SkillCatalog, sheet: Sheet) -> ResolvedSkill:
    hit = catalog.find(read.name)
    if hit:
        heals = hit.kind == "Recovery" or (hit.tier == "unique" and "recover" in hit.text.lower())
        own = hit.tier == "unique" and _is_own_unique(hit.owner, sheet)
        inherited = hit.tier == "unique" and not own
        if not heals:
            pct = 0.0
        elif hit.tier == "rare" or own:
            pct = HEAL_GOLD
        else:  # white recovery, or an inherited unique, which counts as a normal skill
            pct = HEAL_WHITE
        return ResolvedSkill(read.name, hit.tier, hit.kind, hit.scope, True, pct, own, inherited)
    # Not in the docs: fall back to what the row looked like (colour and icon). Only a recovery icon matters here.
    tier = _RARITY_TIER.get(read.rarity or "", "")
    kind = _ICON_KIND.get(read.icon or "", "")
    pct = 0.0
    if kind == "Recovery":
        pct = HEAL_GOLD if tier == "rare" else HEAL_WHITE
    return ResolvedSkill(read.name, tier or "unknown", kind or "unknown", (), False, pct)


def applies(skill: ResolvedSkill, target: Target) -> bool:
    for tag in skill.scope:
        if tag in DISTANCES and tag != target.distance:
            return False
        if tag in STYLES and tag != target.style:
            return False
        if tag in SURFACES and target.surface and tag != target.surface:
            return False
    return True


# --------------------------------------------------------------------------- findings and report

_RANK = {"good": 0, "info": 0, "ok": 1, "warn": 2, "bad": 3}
_ICONS = {"good": "\u2705", "ok": "\U0001F7E1", "warn": "\u26a0\ufe0f", "bad": "\u274c", "info": "\u2139\ufe0f"}


@dataclass
class Finding:
    area: str
    status: str  # good | ok | warn | bad | info
    text: str
    source: str = ""


@dataclass
class TargetReport:
    target: Target
    verdict: str
    findings: list[Finding]
    rank: int
    shortfall: float  # best-case Stamina shortfall over the courses checked (0 if none)


@dataclass
class Report:
    sheet: Sheet
    cap: int
    headline: str
    general: list[Finding]
    targets: list[TargetReport]
    skills: list[ResolvedSkill]
    caveats: list[str] = field(default_factory=list)


def _grade_status(grade: str | None) -> str:
    if grade is None:
        return "info"
    i = GRADES.index(grade)
    return "good" if i <= 1 else "warn" if i == 2 else "bad"


def _stamina_check(sheet: Sheet, course: Course, target: Target, gold_eq: float) -> tuple[Finding, float]:
    stamina = base_stat(sheet.stats["stamina"])
    guts = base_stat(sheet.stats["guts"])
    need, extrap = required_stamina(course, target.style, gold_eq)
    adj_lo, adj_hi = guts_adjustment(guts, course.baseline_guts, course.threshold_guts)
    eff_lo, eff_hi = stamina + adj_lo, stamina + adj_hi
    detail = (f"{course.label}: needs ~{need:.0f} with {gold_eq:.2f} gold-recovery equivalents"
              f"{' (extrapolated past the guide table)' if extrap else ''}; she has {stamina:.0f} + {adj_lo:.0f} to "
              f"{adj_hi:.0f} from her Guts = ~{eff_lo:.0f}-{eff_hi:.0f}.")
    best_short, worst_short = need - eff_hi, need - eff_lo
    if eff_lo >= need:
        status, verdict = "good", "enough"
    elif eff_hi >= need:
        status, verdict = "ok", f"borderline (up to ~{worst_short:.0f} short, depends on how Guts converts)"
    elif best_short <= 100:
        status, verdict = "warn", f"slightly short by ~{best_short:.0f}-{worst_short:.0f}"
    elif best_short <= 300:
        status, verdict = "bad", f"short by ~{best_short:.0f}-{worst_short:.0f}"
    else:
        status, verdict = "bad", f"short by ~{best_short:.0f}-{worst_short:.0f}; 300+ under the guide says Speed stops mattering"
    return Finding("Stamina", status, f"{detail} That is {verdict}.", "Part 2 s2.4"), max(best_short, 0.0)


def evaluate(sheet: Sheet, *, cap: int = DEFAULT_CAP, goal: Goal | None = None,
             catalog: SkillCatalog | None = None) -> Report:
    catalog = catalog or default_catalog()
    goal = goal or Goal()
    resolved = [resolve_skill(s, catalog, sheet) for s in sheet.skills]
    unknown = [r.name for r in resolved if not r.known]
    caveats: list[str] = []

    # ---- target-independent findings
    general: list[Finding] = []
    if "speed" in sheet.stats:
        raw = sheet.stats["speed"]
        base = base_stat(raw)
        pct = raw / cap * 100
        status = "good" if pct >= 90 else "ok" if pct >= 75 else "warn"
        general.append(Finding("Speed", status,
                               f"Speed {raw} counts as ~{base:.0f} (raw above 1200 is halved); that is {pct:.0f}% of the {cap} cap "
                               "(guide: aim for the scenario cap).", "Part 2 s2.1, s2.3"))
    if "power" in sheet.stats:
        power = base_stat(sheet.stats["power"])
        status = "good" if power >= 1200 else "ok" if power >= 1000 else "warn"
        general.append(Finding("Power", status, f"Power {sheet.stats['power']} counts as ~{power:.0f}; the guide's general goal is 1200.",
                               "Part 2 s2.3"))
    if "wit" in sheet.stats:
        wit = base_stat(sheet.stats["wit"])
        status = "good" if wit >= 300 else "warn"
        general.append(Finding("Wit", status,
                               f"Wit {sheet.stats['wit']}: skills activate ~{skill_activation_pct(wit):.1f}% of the time and she is "
                               f"Rushed ~{rushed_pct(wit)}% of races. The Global guide says 300-500 is enough (JP pushes 1200+).",
                               "Part 2 s2.3, s2.9"))
    if not sheet.skills_seen:
        general.append(Finding("Skills", "info", "No Skills tab screenshot was included, so skills were not judged "
                                                 "(that also means no recoveries were counted for Stamina)."))
    if unknown:
        general.append(Finding("Skills", "info",
                               f"{len(unknown)} skill(s) are not in my skill docs: {', '.join(unknown)}. "
                               "I counted them only if their icon showed a recovery."))
    own_unique = [r for r in resolved if r.own_unique]
    if own_unique:
        general.append(Finding("Unique", "info", f"Her unique, {own_unique[0].name}"
                                                 f"{f' (Lvl {sheet.unique_level})' if sheet.unique_level else ''}, is in the docs but its "
                                                 "effect size isn't, so it was not scored."))

    # ---- per target
    targets, notes = pick_targets(sheet, goal)
    caveats += notes
    reports: list[TargetReport] = []
    for t in targets:
        findings: list[Finding] = []
        apt = sheet.aptitudes
        parts = []
        statuses = []
        if t.surface:
            g = apt.get(t.surface)
            parts.append(f"{SURFACE_LABEL[t.surface]} {g or '?'} (accel {_SURFACE_MOD.get(g, '?')})")
            statuses.append(_grade_status(g))
        g = apt.get(t.distance)
        parts.append(f"{DISTANCE_LABEL[t.distance]} {g or '?'} (speed {_DISTANCE_MOD.get(g, '?')})")
        statuses.append(_grade_status(g))
        g = apt.get(t.style)
        parts.append(f"{STYLE_LABEL[t.style]} {g or '?'} (Wit {_STYLE_MOD.get(g, '?')})")
        statuses.append(_grade_status(g))
        worst = max(statuses, key=lambda s: _RANK[s])
        findings.append(Finding("Aptitude", worst, ", ".join(parts) + ".", "Part 2 s2.2"))

        recoveries = [r for r in resolved if r.heal_pct and applies(r, t)]
        gold_eq = sum(r.heal_pct for r in recoveries) / HEAL_GOLD
        off_target = [r.name for r in resolved if r.known and not applies(r, t)]
        if sheet.skills_seen:
            listed = ", ".join(f"{r.name} {r.heal_pct:g}%" for r in recoveries) or "none"
            findings.append(Finding("Recoveries", "info", f"Counted for this target: {listed} = {gold_eq:.2f} gold-equivalents "
                                                          f"(gold {HEAL_GOLD:g}%, white {HEAL_WHITE:g}% of max HP).", "Part 2 s2.4"))
            if off_target:
                findings.append(Finding("Off-target skills", "info", f"Won't work here (wrong distance, style or surface): {', '.join(off_target)}."))

        shortfall = 0.0
        if "stamina" in sheet.stats and "guts" in sheet.stats:
            for course in COURSES:
                if course.distance != t.distance:
                    continue
                finding, short = _stamina_check(sheet, course, t, gold_eq)
                findings.append(finding)
                shortfall = max(shortfall, short)
        else:
            findings.append(Finding("Stamina", "info", "Stamina or Guts wasn't readable, so Stamina was not checked."))

        rank = max(_RANK[f.status] for f in findings)
        verdict = {0: "Good", 1: "Decent", 2: "Mixed", 3: "Not good"}[rank]
        reports.append(TargetReport(t, verdict, findings, rank, shortfall))

    reports.sort(key=lambda r: (r.rank, r.shortfall))
    if reports:
        best = reports[0]
        if best.rank >= 3:
            headline = "No target looks good for this build as it stands"
            if best.shortfall:
                headline += f" (closest: {best.target.label}, Stamina ~{best.shortfall:.0f} short)"
        else:
            headline = f"Best fit: {best.target.label} - {best.verdict.lower()}"
            others = [r for r in reports[1:] if r.rank >= 3]
            if others:
                headline += f". Not good for: {', '.join(r.target.label for r in others)}"
    else:
        headline = "I couldn't pick a target to judge"

    caveats += [
        "Required Stamina comes from the guide's table (built for 1200 Speed/Power, 600 Wit, no downhills) and is interpolated by "
        "recovery amount, so treat it as an estimate: the guide says calculators differ by 100-200.",
        "Judged as a finished runner without the +400 training bonus. Skill timing, sparks, the support deck and JP-only "
        "mechanics (Wit Limit Break) were not checked.",
    ]
    return Report(sheet, cap, headline, general, reports, resolved, caveats)


def render_report(report: Report) -> str:
    s = report.sheet
    lines: list[str] = []
    title = s.trainee or "Trainee"
    if s.outfit:
        title += f" [{s.outfit}]"
    if s.rating:
        title += f" - rating {s.rating:,}"
    lines.append(f"**{title}**")
    if s.stats:
        lines.append("I read: " + " | ".join(f"{k.title()} {s.stats[k]}" for k in STATS if k in s.stats))
    if s.aptitudes:
        def grp(keys, labels):
            return ", ".join(f"{labels[k]} {s.aptitudes[k]}" for k in keys if k in s.aptitudes)
        lines.append("Aptitudes: " + " | ".join(x for x in (
            grp(SURFACES, SURFACE_LABEL), grp(DISTANCES, DISTANCE_LABEL), grp(STYLES, STYLE_LABEL)) if x))
    if s.skills_seen:
        lines.append(f"Skills read: {len(s.skills)}")
    lines.append(f"(Stat cap assumed: {report.cap}. Nothing from this screenshot is saved.)")
    lines.append("")
    lines.append(f"**Verdict: {report.headline}.**")
    for tr in report.targets:
        lines.append("")
        lines.append(f"**{tr.target.label} - {tr.verdict}**")
        for f in tr.findings:
            lines.append(f"{_ICONS[f.status]} {f.area}: {f.text}")
    if report.general:
        lines.append("")
        lines.append("**Other checks**")
        for f in report.general:
            lines.append(f"{_ICONS[f.status]} {f.text}")
    if s.notes:
        lines.append("")
        lines.append("**Reading notes** (check these against your screen)")
        lines += [f"- {n}" for n in s.notes]
    lines.append("")
    lines += [f"_{c}_" for c in report.caveats]
    return "\n".join(lines)
