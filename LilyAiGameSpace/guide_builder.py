"""Builds a guide from the Umamusume docs without letting the model free-write it.

The engine does the retrieval and the model only writes from what it is handed:

    1. plan()     resolve the subject (no model call) and pick an outline (fixed template, or the doc's own headings)
    2. gather     per outline item: search + read passages, tagged [S1], [S2]...
       prep       (sandbox) pick the parts of those passages that best fit each section within the budget, and compute exact
                  figures for numeric tables, tagged [C1], [C2]... Falls back to the old clipped passages if it can't run.
    3. write      one small model call per section, grounded only in that section's passages
    4. verify     (sandbox) no-model check: any sentence whose numbers aren't in the passages is dropped, bad tags removed.
                  Falls back to verify_section() below, which is the same rule.
    5. assemble   title + sections + a Sources footer built from the passages actually cited
    6. cache      build_and_store() saves successful guides; errors are never saved (see GuideCacheStore)

Section calls run one after another (free-tier Groq limits), and a section with no passages costs no call.
If any section's model call fails after one retry the whole build fails with ok=False and nothing is cached.

The sandbox steps use sandbox_scripts/guide_ops.py: two PandaStack boots per guide (one prep, one verify) instead of one per
section. The model API key never goes to the sandbox, only doc text and the drafted sections. Set LILYAI_GUIDE_SANDBOX=0 to
turn the sandbox steps off (the guide is then built exactly as before).
"""
from __future__ import annotations

import asyncio
import hashlib
import os
import re
from dataclasses import dataclass, field
from typing import Any, Protocol

from LilyAiCore.Exceptions.errors import ProviderError, RateLimitError
from LilyAiCore.Helpers.clock import now_ts
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiGameSpace import sandbox_runner
from LilyAiGameSpace.number_check import BULLET as _BULLET
from LilyAiGameSpace.number_check import TAG as _TAG
from LilyAiGameSpace.number_check import numbers_in
from LilyAiGameSpace.Umamusume.UmamusumeGameSpaceEngine import Doc, UmamusumeGameSpaceEngine, get_engine

log = get_logger("gamespace.guide")

MAX_SECTIONS = 6
SECTION_CHARS = 3000       # passage text handed to the model per section
MAX_PASSAGE_CHARS = 2000
MAX_PASSAGES = 5
MAX_SECTION_TOKENS = 650
# What is read before the sandbox picks the useful parts (only used when the sandbox step is on).
RAW_SECTION_CHARS = 24000
RAW_PASSAGE_CHARS = 12000
RAW_MAX_PASSAGES = 6
MAX_FACTS = 3              # exact table figures per section

NO_DATA = "_The docs don't cover this yet._"
GENERIC_ERROR = (
    "I couldn't finish that guide - my language model had trouble partway through. "
    "Nothing was saved, so just ask again in a minute."
)
OFFLINE_ERROR = "I can't build guides right now because my language model isn't connected (no GROQ_API_KEY is set)."
NOTHING_FOUND = "I couldn't find anything in the game docs to build that guide from."

_SYSTEM = (
    "You write ONE section of an Umamusume guide. Your only source of facts is the numbered passages in the "
    "user message. Rules:\n"
    "1. Use only facts stated in the passages. No outside knowledge, no guessing. Skip anything the passages don't say.\n"
    "2. Copy numbers, names, skill names, stats and percentages exactly as written. Never round, convert or invent a number.\n"
    "3. If passages disagree, show both values and say which source tag each one comes from.\n"
    "4. Put the source tag, like [S2], right after each fact it supports.\n"
    "5. Ignore passages that aren't about the guide's subject.\n"
    "6. Output only the section body: short markdown bullets or short paragraphs, under 180 words, "
    "no heading, no intro or outro.\n"
    "7. If the passages contain nothing useful for this section, output exactly: NO_DATA\n"
    "8. A passage tagged like [C1] holds exact figures calculated from a table in the docs. You may quote those figures "
    "and cite the tag like any other source."
)

# (title, what it should cover, queries). {s} = subject, {g} = goal; empty parts are collapsed away.
_CHARACTER = (
    ("Overview", "Who this character is and what role or running style the docs say suits them.",
     ("{s}", "{s} overview profile")),
    ("Aptitudes & Growth", "Track, distance and running-style aptitudes and growth rates, exactly as listed.",
     ("{s} aptitude growth rate stats", "aptitude growth rate")),
    ("Skills", "The unique skill and other skills the docs mention, and what each one does.",
     ("{s} skills unique skill",)),
    ("Support Cards & Deck", "Support cards or deck advice the docs give for this character.",
     ("{s} support card deck", "support card deck recommendation")),
    ("Training Plan", "How to train this character: priorities, strategy and scenario notes.",
     ("{s} training strategy {g}", "training strategy {g}")),
    ("Races & Objectives", "Race objectives, schedule and target races.",
     ("{s} race objectives schedule", "race schedule objectives {g}")),
)
_GENERIC = (
    ("Overview", "What this is and why it matters.", ("{s}", "{s} overview")),
    ("How It Works", "The key mechanics and rules.", ("{s} mechanics how it works", "{s} rules")),
    ("Recommended Strategy", "Concrete recommended steps or setups.", ("{s} strategy recommended {g}", "{s} best setup {g}")),
    ("Tips & Common Mistakes", "Practical tips and pitfalls to avoid.", ("{s} tips mistakes avoid",)),
)
_SKIP_HEADINGS = frozenset({"sources", "images", "references", "see also", "changelog", "contents", "table of contents"})

# Words that make a message a guide request rather than part of the subject.
_INTENT_WORDS = frozenset(
    "make build create write generate draft prepare compile give put together guide guides walkthrough please can "
    "could would you i me my want need a an the for on about to of and with new full complete detailed short quick "
    "step by is some your own us".split()
)


def _sandbox_default() -> bool:
    return os.getenv("LILYAI_GUIDE_SANDBOX", "1").strip().lower() not in ("0", "false", "no", "off")


class GuideCache(Protocol):
    def get(self, key: str) -> Any: ...
    def put(self, key: str, *, title: str, question: str, content: str, model: str,
            source_ids: list[str], docs_sig: str, ok: bool) -> bool: ...
    def mark_used(self, key: str) -> None: ...


@dataclass
class SectionSpec:
    title: str
    instruction: str
    queries: tuple[str, ...]
    reads: tuple[tuple[str, str], ...] = ()   # (doc id, section path) read directly before searching


@dataclass
class GuidePlan:
    key: str
    title: str
    subject: str
    goal: str
    subject_ids: list[str]
    outline: list[SectionSpec]
    question: str


@dataclass
class Passage:
    tag: str
    doc_id: str
    title: str
    section: str
    text: str


@dataclass
class GuideResult:
    ok: bool
    text: str
    title: str = ""
    model: str = ""
    from_cache: bool = False
    saved: bool = False
    stale: bool = False
    note: str = ""
    sections: list[str] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)
    dropped: int = 0
    created_at: float = 0.0


class _BuildFailed(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class _Registry:
    """Hands out one global tag per (doc, section) so [S3] means the same passage everywhere in a guide."""

    def __init__(self) -> None:
        self._tags: dict[tuple[str, str], str] = {}
        self.info: dict[str, tuple[str, str, str, str]] = {}  # tag -> (doc id, title, section, url)
        self.computed: dict[str, tuple[str, str]] = {}        # [C#] tag -> (where the table is, doc id)

    def tag(self, doc_id: str, title: str, section: str, url: str) -> str:
        k = (doc_id, section)
        if k not in self._tags:
            t = f"S{len(self._tags) + 1}"
            self._tags[k] = t
            self.info[t] = (doc_id, title, section, url)
        return self._tags[k]


# ------------------------------------------------------------------ small text helpers
def _words(text: str) -> list[str]:
    return re.findall(r"\w+", text.replace("_", " ").casefold())


def _stem(word: str) -> str:
    return word[:-1] if len(word) > 3 and word.endswith("s") and not word.endswith("ss") else word


def _age(ts: float) -> str:
    secs = max(0.0, now_ts() - ts)
    if secs < 3600:
        return f"{max(1, int(secs // 60))} min ago"
    if secs < 48 * 3600:
        return f"{int(secs // 3600)} hours ago"
    return f"{int(secs // 86400)} days ago"


def _has_content(body: str) -> bool:
    return len(re.sub(r"[\W_]+", "", _TAG.sub("", body))) >= 15


def verify_section(text: str, passages: list[Passage]) -> tuple[str, int]:
    """No-model check on a drafted section. Returns (cleaned text, number of dropped sentences/lines).

    Citation tags the passages don't have are removed; any line (or sentence, when a line has several)
    containing a number that appears nowhere in the passages is dropped.
    """
    tags = {p.tag for p in passages}
    allowed: set[str] = set()
    for p in passages:
        allowed |= numbers_in(f"{p.title} {p.section} {p.text}")
    text = _TAG.sub(lambda m: m.group(0) if m.group(1) in tags else "", text)

    kept: list[str] = []
    dropped = 0
    for line in text.splitlines():
        if not line.strip() or numbers_in(line) <= allowed:
            kept.append(line.rstrip())
            continue
        parts = re.split(r"(?<=[.!?])\s+", line.strip())
        if len(parts) == 1:
            dropped += 1
            continue
        good = [p for p in parts if numbers_in(p) <= allowed]
        dropped += len(parts) - len(good)
        if good:
            joined = " ".join(good)
            m = _BULLET.match(line)
            if m and not _BULLET.match(joined):
                joined = m.group(0) + joined
            kept.append(joined)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip(), dropped


def _is_offline(resp: Any) -> bool:
    return getattr(resp, "model", "") == "offline" or (getattr(resp, "content", "") or "").startswith("(offline mode")


def _heading_outline(doc: Doc, subject: str) -> list[SectionSpec]:
    """Outline taken from a doc's own level-2 headings (for guide-style docs that already have structure)."""
    secs = doc.visible()
    specs: list[SectionSpec] = []
    for i, s in enumerate(secs):
        if s.level != 2 or s.key in _SKIP_HEADINGS:
            continue
        size = len(s.text)
        for nxt in secs[i + 1:]:
            if nxt.level <= 2:
                break
            size += len(nxt.text)
        if size < 80:
            continue
        specs.append(SectionSpec(s.heading, f"What the docs say under '{s.heading}'.",
                                 (f"{subject} {s.heading}",), reads=((doc.id, s.path),)))
    return specs


def _section_prompt(plan: GuidePlan, spec: SectionSpec, passages: list[Passage]) -> str:
    blocks = "\n\n".join(f"[{p.tag}] {p.title} > {p.section}\n{p.text}" for p in passages)
    return (
        f"Guide: {plan.title}\nSubject: {plan.subject}\nReader's goal: {plan.goal or 'a general guide'}\n"
        f"Section: {spec.title}\nThis section should cover: {spec.instruction}\n\n"
        f"Source passages:\n\n{blocks}\n\nWrite the \"{spec.title}\" section now."
    )


class GuideBuilder:
    def __init__(self, engine: UmamusumeGameSpaceEngine | None, provider: LLMProvider, model: str,
                 cache: GuideCache, *, pause_s: float = 0.0, retry_delay: float = 1.5,
                 use_sandbox: bool | None = None):
        self._engine = engine
        self.provider, self.model, self.cache = provider, model, cache
        self.pause_s, self.retry_delay = pause_s, retry_delay
        # None = follow LILYAI_GUIDE_SANDBOX (on by default). The sandbox steps fall back to local code on any problem.
        self.use_sandbox = _sandbox_default() if use_sandbox is None else use_sandbox
        self._locks: dict[str, asyncio.Lock] = {}

    @property
    def engine(self) -> UmamusumeGameSpaceEngine:
        return self._engine or get_engine()

    # ------------------------------------------------------------- 1. plan
    def plan(self, text: str) -> GuidePlan | None:
        """Resolve what the guide is about. None when the message names nothing the docs know."""
        eng = self.engine
        docs = eng.mentioned_docs(text)[:2]
        topic = [w for w in _words(text) if w not in _INTENT_WORDS]
        if not docs and topic:
            d = eng.resolve(" ".join(topic))
            docs = [d] if d else []

        if docs:
            primary = docs[0]
            names = set().union(*(d.name_terms for d in docs))
            goal_words = [w for w in topic if _stem(w) not in names and w not in names]
            subject = " & ".join(d.title for d in docs)
            subject_ids = [d.id for d in docs]
            goal = " ".join(goal_words)
            key_terms = goal_words
        else:
            if not topic or not eng.search(" ".join(topic), None, 1):
                return None
            primary, goal = None, ""
            subject, subject_ids, key_terms = " ".join(topic).title(), [], topic

        key_raw = "|".join(sorted(subject_ids)) + "::" + " ".join(sorted({_stem(w) for w in key_terms}))
        title = f"{subject} Guide" + (f" ({goal})" if goal else "")
        return GuidePlan(
            key=hashlib.sha1(key_raw.encode("utf-8")).hexdigest()[:24], title=title, subject=subject, goal=goal,
            subject_ids=subject_ids, outline=self._outline(primary, subject, goal), question=text,
        )

    @staticmethod
    def _outline(primary: Doc | None, subject: str, goal: str) -> list[SectionSpec]:
        if primary is not None and primary.category.casefold() == "character":
            template = _CHARACTER
        else:
            if primary is not None:
                heads = _heading_outline(primary, subject)
                if len(heads) >= 3:
                    return heads[:MAX_SECTIONS]
            template = _GENERIC
        return [
            SectionSpec(t, ins, tuple(" ".join(q.format(s=subject, g=goal).split()) for q in qs))
            for t, ins, qs in template
        ]

    # ------------------------------------------------------------- 2. gather (+ prep)
    def _gather(self, spec: SectionSpec, subject_ids: list[str], reg: _Registry, *, raw: bool = False) -> list[Passage]:
        """Passages for one section. raw=True reads much more text per passage, for the sandbox to choose from."""
        eng = self.engine
        out: list[Passage] = []
        covered: dict[str, list[str]] = {}
        budget = RAW_SECTION_CHARS if raw else SECTION_CHARS
        per_passage = RAW_PASSAGE_CHARS if raw else MAX_PASSAGE_CHARS
        max_passages = RAW_MAX_PASSAGES if raw else MAX_PASSAGES

        def add(doc_id: str, section: str | None) -> None:
            nonlocal budget
            if budget < 400 or len(out) >= max_passages:
                return
            r = eng.read(doc_id, section, min(budget, per_passage))
            if r is None or not r.text.strip():
                return
            path = r.section or ""
            for prev in covered.get(r.doc_id, []):
                if path == prev or (prev and path.startswith(prev + " > ")):
                    return  # already inside a section we read
            if any(r.text == p.text for p in out):
                return
            tag = reg.tag(r.doc_id, r.title, path or "Overview", r.sources[0] if r.sources else "")
            out.append(Passage(tag, r.doc_id, r.title, path or "Overview", r.text))
            covered.setdefault(r.doc_id, []).append(path)
            budget -= len(r.text)

        for doc_id, section in spec.reads:
            add(doc_id, section)
        for q in spec.queries:
            hits = eng.search(q, None, 6)
            if not hits:
                continue
            floor = hits[0].score * 0.5
            for h in hits:
                if h.doc_id in subject_ids or h.score >= floor:
                    add(h.doc_id, h.section)
        return out

    async def _prepare(self, plan: GuidePlan, reg: _Registry) -> list[list[Passage]] | None:
        """One sandbox run for the whole outline: per section, the best parts of the raw passages plus exact table figures.
        None means "use the ordinary clipped passages" (sandbox step off, or anything went wrong)."""
        if not self.use_sandbox:
            return None
        try:
            raws = [self._gather(spec, plan.subject_ids, reg, raw=True) for spec in plan.outline]
            if not any(raws):
                return None
            params = {
                "op": "prep", "budget": SECTION_CHARS, "max_facts": MAX_FACTS,
                "sections": [
                    {"title": spec.title, "queries": [spec.title, plan.goal, *spec.queries],
                     "passages": [{"tag": p.tag, "doc": p.title, "section": p.section, "text": p.text} for p in ps]}
                    for spec, ps in zip(plan.outline, raws)
                ],
            }
            result, in_box = await sandbox_runner.run_guide_ops_ex_async(params)
            sections = result["sections"]
            if len(sections) != len(raws):
                raise ValueError("wrong number of sections back")
            out: list[list[Passage]] = []
            for ps, sec in zip(raws, sections):
                by_tag = {p.tag: p for p in ps}
                kept: list[Passage] = []
                for item in sec.get("passages") or []:
                    src = by_tag.get(item.get("tag"))
                    text = str(item.get("text") or "").strip()
                    if src and text:
                        kept.append(Passage(src.tag, src.doc_id, src.title, src.section, text))
                for fact in sec.get("facts") or []:
                    tag, text = str(fact.get("tag") or ""), str(fact.get("text") or "").strip()
                    if re.fullmatch(r"C\d+", tag) and text:
                        origin = reg.info.get(str(fact.get("from") or ""))
                        reg.computed[tag] = (str(fact.get("source") or ""), origin[0] if origin else "")
                        kept.append(Passage(tag, "computed", "Computed", str(fact.get("source") or ""), text))
                out.append(kept)
            log.info("guide prep done %s for %d sections", "in the sandbox" if in_box else "locally", len(out))
            return out
        except Exception as e:
            log.warning("guide prep failed (%s: %s); using the clipped passages", type(e).__name__, str(e)[:200])
            return None

    # ------------------------------------------------------------- 3. write
    async def _write(self, plan: GuidePlan, spec: SectionSpec, passages: list[Passage]) -> tuple[str, str]:
        messages = [
            {"role": "system", "content": _SYSTEM},
            {"role": "user", "content": _section_prompt(plan, spec, passages)},
        ]
        for _ in range(2):
            try:
                resp = await self.provider.chat(messages, model=self.model, temperature=0.2,
                                                max_tokens=MAX_SECTION_TOKENS)
            except RateLimitError as e:
                log.warning("guide section %r rate limited: %s", spec.title, e)
                await asyncio.sleep(min(float(e.retry_after or 3), 20.0) if self.retry_delay else 0)
                continue
            except ProviderError as e:
                log.warning("guide section %r failed: %s", spec.title, e)
                await asyncio.sleep(self.retry_delay)
                continue
            if _is_offline(resp):
                raise _BuildFailed(OFFLINE_ERROR)
            content = (resp.content or "").strip()
            if content:
                return content, resp.model or self.model
            log.warning("guide section %r came back empty", spec.title)
            await asyncio.sleep(self.retry_delay)
        raise _BuildFailed(GENERIC_ERROR)

    # ------------------------------------------------------------- 4. verify
    async def _verify_all(self, drafts: list[tuple[SectionSpec, str, list[Passage]]]) -> list[tuple[str, int]]:
        """(cleaned text, dropped) per draft, in order. One sandbox run for all the drafts; verify_section() if that fails."""
        out: list[tuple[str, int]] = [("", 0)] * len(drafts)
        todo = [(i, raw, ps) for i, (_, raw, ps) in enumerate(drafts)
                if ps and not raw.strip().upper().startswith("NO_DATA")]
        if not todo:
            return out
        results: list[tuple[str, int]] | None = None
        if self.use_sandbox:
            try:
                params = {"op": "verify", "sections": [
                    {"text": raw, "tags": [p.tag for p in ps], "allowed": [f"{p.title} {p.section} {p.text}" for p in ps]}
                    for _, raw, ps in todo]}
                result, _ = await sandbox_runner.run_guide_ops_ex_async(params)
                secs = result["sections"]
                if len(secs) != len(todo):
                    raise ValueError("wrong number of sections back")
                results = [(str(s["text"]), int(s["dropped"])) for s in secs]
            except Exception as e:
                log.warning("guide verify in the sandbox failed (%s: %s); verifying locally", type(e).__name__, str(e)[:200])
                results = None
        if results is None:
            results = [verify_section(raw, ps) for _, raw, ps in todo]
        for (i, _, _), res in zip(todo, results):
            out[i] = res
        return out

    # ------------------------------------------------------------- 5. assemble
    async def build(self, plan: GuidePlan) -> GuideResult:
        """Build one guide. Never raises; any failure is ok=False with a user-facing message (and is never cached)."""
        reg = _Registry()
        drafts: list[tuple[SectionSpec, str, list[Passage]]] = []
        model, called = "", 0
        try:
            prepped = await self._prepare(plan, reg)
            for i, spec in enumerate(plan.outline):
                mine = prepped[i] if prepped is not None else []
                passages = mine if any(not p.tag.startswith("C") for p in mine) else self._gather(spec, plan.subject_ids, reg)
                if not passages:
                    drafts.append((spec, "", []))
                    continue
                if called and self.pause_s:
                    await asyncio.sleep(self.pause_s)
                raw, used_model = await self._write(plan, spec, passages)
                called += 1
                model = model or used_model
                drafts.append((spec, raw, passages))
            verified = await self._verify_all(drafts)
        except _BuildFailed as e:
            return GuideResult(False, e.message, title=plan.title)
        except Exception:
            log.exception("guide build crashed")
            return GuideResult(False, GENERIC_ERROR, title=plan.title)

        bodies: list[tuple[str, str]] = []
        used_tags: list[str] = []
        dropped, data = 0, 0
        for (spec, raw, passages), (body, d) in zip(drafts, verified):
            if not passages:
                bodies.append((spec.title, NO_DATA))
                continue
            dropped += d
            if raw.strip().upper().startswith("NO_DATA") or not _has_content(body):
                bodies.append((spec.title, NO_DATA))
                continue
            bodies.append((spec.title, body))
            used_tags.extend(p.tag for p in passages)
            data += 1
        if not data:
            return GuideResult(False, NOTHING_FOUND, title=plan.title)

        parts = [f"# {plan.title}"]
        if plan.goal:
            parts.append(f"_Focus: {plan.goal}_")
        parts += [f"## {t}\n{b}" for t, b in bodies]
        cited = list(dict.fromkeys(_TAG.findall("\n".join(b for _, b in bodies)))) or list(dict.fromkeys(used_tags))
        lines = []
        source_ids: list[str] = []
        for t in cited:
            if t in reg.info:
                doc_id, title, section, url = reg.info[t]
                source_ids.append(doc_id)
                lines.append(f"[{t}] {title} > {section}" + (f" - <{url}>" if url else ""))
            elif t in reg.computed:
                where, doc_id = reg.computed[t]
                if doc_id:
                    source_ids.append(doc_id)
                lines.append(f"[{t}] Computed from {where} (exact figures calculated from the table)")
        parts.append("---\n**Sources** (game docs)\n" + "\n".join(lines))
        parts.append("_Built only from the game docs; anything they don't say is left out._")
        return GuideResult(
            True, "\n\n".join(parts), title=plan.title, model=model, sections=[t for t, _ in bodies],
            source_ids=list(dict.fromkeys(source_ids)), dropped=dropped, created_at=now_ts(),
        )

    # ------------------------------------------------------------- 6. cache
    def fingerprint(self, doc_ids: list[str]) -> str:
        """Content hash of the source docs, so a saved guide can be flagged when the docs changed under it."""
        h = hashlib.sha1()
        for doc_id in sorted(set(doc_ids)):
            h.update(doc_id.encode("utf-8"))
            d = self.engine.resolve(doc_id)
            if d is None:
                h.update(b"<gone>")
                continue
            for s in d.sections:
                h.update(s.heading.encode("utf-8"))
                h.update(s.text.encode("utf-8"))
        return h.hexdigest()[:16]

    def lookup(self, plan: GuidePlan) -> Any | None:
        """The saved guide for this question (flagged .stale if the docs changed since), else None."""
        hit = self.cache.get(plan.key)
        if hit is None:
            return None
        hit.stale = bool(hit.source_ids) and self.fingerprint(hit.source_ids) != hit.docs_sig
        return hit

    @staticmethod
    def ask_text(hit: Any) -> str:
        stale = " The game docs have changed since then, so a fresh one may differ." if hit.stale else ""
        return (
            f"I already built this guide before: **{hit.title}** (saved {_age(hit.created_at)}).{stale}\n\n"
            "Want the saved copy, or should I generate a new one?"
        )

    def _from_cache(self, plan: GuidePlan, hit: Any) -> GuideResult:
        self.cache.mark_used(plan.key)
        note = f"Here's the saved guide (built {_age(hit.created_at)})."
        if hit.stale:
            note += " The game docs have changed since, so say \"generate new guide\" if you want it refreshed."
        return GuideResult(
            True, hit.content, title=hit.title, model=hit.model, from_cache=True, saved=True, stale=hit.stale,
            note=note, source_ids=list(hit.source_ids), created_at=hit.created_at,
            sections=re.findall(r"(?m)^## (.+)$", hit.content),
        )

    async def build_and_store(self, plan: GuidePlan, *, force: bool = False) -> GuideResult:
        """Return the saved guide, or build one and save it. force=True always builds a fresh one.

        A failed build is returned as-is and nothing is written, and a failed forced rebuild leaves the
        previously saved guide untouched.
        """
        lock = self._locks.setdefault(plan.key, asyncio.Lock())
        async with lock:
            if not force:
                hit = self.lookup(plan)
                if hit is not None:
                    return self._from_cache(plan, hit)
            result = await self.build(plan)
            if result.ok:
                result.saved = self.cache.put(
                    plan.key, title=result.title, question=plan.question, content=result.text, model=result.model,
                    source_ids=result.source_ids, docs_sig=self.fingerprint(result.source_ids), ok=True,
                )
            return result
