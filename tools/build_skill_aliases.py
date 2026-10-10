#!/usr/bin/env python3
"""
Build tools/sim_data/skill_aliases.json: the names the game shows (Global) -> simulator skill ids.

Why: skills.json uses the datamined upstream English names, many of which are fan translations ("Straight Recovery",
"Archline Professor") while the game shows "Straightaway Recovery" and "Professor of Curvature". A veteran read from a
screenshot carries the game's names, so without this map those skills are silently left out of a simulation.

Source: umamusu.wiki "Game:List of Skills". Every skill name there links to Game:Skills/<id>, and the ids are the same
ids skills.json uses, so the pairing is exact; no guessing from the names. The same page is read the way
build_support_cards.py reads wiki pages (MediaWiki API, parsed HTML).

Owners: the unique skill of a character and its weaker inherited copy share one Global name. The Game8 table in
LilyAiGameSpace/Umamusume/Skill/skill.md says who owns each unique skill, so the simulator can give the owner the
unique one and everyone else the inherited one.

Output (default tools/sim_data/skill_aliases.json):
    names         Global name -> [ids], preferred first (inherited copy before the unique skill)
    unmodelled    Global name -> id, for real skills skills.json has no entry for (effects the simulator cannot model)
    unique_owner  id -> character, for unique skills whose owner is known
Entries already in the file that the wiki page did not return are kept, so hand-added names survive a rebuild.

Usage:
    python tools/build_skill_aliases.py                    # download from umamusu.wiki
    python tools/build_skill_aliases.py --html page.html   # use a saved copy of the parsed page HTML
    python tools/build_skill_aliases.py --dry-run          # print stats, write nothing
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "LilyAiGameSpace" / "Umamusume" / "Simulation"
sys.path.insert(0, str(SIM_DIR))
from Simulator import skill_key  # noqa: E402  (the resolver's own normalisation, so both always agree)

WIKI_API = "https://umamusu.wiki/w/api.php"
PAGE = "Game:List_of_Skills"
UA = "DmLilyAi-skill-aliases/1.0 (personal project, github.com/UmakraftCircle/DmLilyAi)"
DEFAULT_DATA = ROOT / "tools" / "sim_data"
SKILL_MD = ROOT / "LilyAiGameSpace" / "Umamusume" / "Skill" / "skill.md"
MIN_NAMES = 300   # a page far smaller than this means the wiki layout changed; fail loudly

_ID_RE = re.compile(r"Game:Skills/(\d+)(?:[/?#\"']|$)")


class SkillLinks(HTMLParser):
    """Collects (id, link text) for every <a> that points at Game:Skills/<id> and has visible text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found: list[tuple[str, str]] = []
        self._id: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        a = dict(attrs)
        m = _ID_RE.search(urllib.parse.unquote(a.get("href") or "")) or _ID_RE.search(a.get("title") or "")
        self._id, self._text = (m.group(1) if m else None), []

    def handle_data(self, data):
        if self._id is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._id is not None:
            text = " ".join("".join(self._text).split())
            if text:
                self.found.append((self._id, text))
            self._id = None


def parse_links(html: str) -> list[tuple[str, str]]:
    p = SkillLinks()
    p.feed(html)
    return p.found


def fetch_page_html() -> str:
    qs = urllib.parse.urlencode({"action": "parse", "page": PAGE, "prop": "text", "format": "json",
                                 "formatversion": 2, "redirects": 1, "disableeditsection": 1})
    req = urllib.request.Request(f"{WIKI_API}?{qs}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))["parse"]["text"]


def is_inherited(sid: str) -> bool:
    return len(sid) == 6 and sid.startswith("9")


def game8_unique_owners(md: str) -> dict[str, str]:
    """Global unique skill name -> owning character, from the 'Unique Skills' table of skill.md."""
    out, in_unique = {}, False
    for line in md.splitlines():
        if line.startswith("## "):
            in_unique = line[3:].strip().lower().startswith("unique")
            continue
        if not in_unique or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "skill name" or set(cells[0]) <= set("-: "):
            continue
        m = re.match(r"Innate:\s*(.+?)\s*(?:\(.*\))?\s*$", cells[-1])
        if m:
            out[cells[0]] = m.group(1)
    return out


def build(links: list[tuple[str, str]], skills: dict, owners: dict[str, str], previous: dict | None = None) -> dict:
    """Pure function: wiki links + skills.json + owners -> the alias document."""
    names: dict[str, list[str]] = {}
    unmodelled: dict[str, str] = {}
    first_text: dict[str, str] = {}
    for sid, text in links:
        first_text.setdefault(sid, text)
    for sid, text in first_text.items():
        if sid in skills:
            ids = names.setdefault(text, [])
            if sid not in ids:
                ids.append(sid)
        else:
            unmodelled.setdefault(text, sid)
    for text, ids in names.items():
        ids.sort(key=lambda i: (not is_inherited(i), i))   # inherited copy first, then the rest by id
        unmodelled.pop(text, None)

    unique_owner: dict[str, str] = {}
    by_key = {skill_key(n): ids for n, ids in names.items()}
    for uname, owner in owners.items():
        for sid in by_key.get(skill_key(uname), []):
            if not is_inherited(sid):
                unique_owner[sid] = owner

    if previous:   # keep hand-added entries the page did not return
        for text, ids in (previous.get("names") or {}).items():
            if skill_key(text) not in {skill_key(n) for n in names}:
                names[text] = [str(i) for i in ids if str(i) in skills]
        for text, sid in (previous.get("unmodelled") or {}).items():
            if skill_key(text) not in {skill_key(n) for n in list(names) + list(unmodelled)}:
                unmodelled[text] = str(sid)
        for sid, owner in (previous.get("unique_owner") or {}).items():
            unique_owner.setdefault(str(sid), owner)

    return {
        "_comment": "In-game (Global) skill names -> simulator skill ids. Built by tools/build_skill_aliases.py from "
                    "umamusu.wiki; 'names' lists preferred ids first; 'unmodelled' are real skills the simulator has no "
                    "effect data for; 'unique_owner' says whose unique skill an id is.",
        "version": 1,
        "names": dict(sorted(names.items(), key=lambda kv: kv[0].lower())),
        "unmodelled": dict(sorted(unmodelled.items(), key=lambda kv: kv[0].lower())),
        "unique_owner": dict(sorted(unique_owner.items())),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--html", help="saved parsed-page HTML instead of downloading")
    ap.add_argument("--out", default=str(DEFAULT_DATA), help="folder holding skills.json and skill_aliases.json")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    out_dir = Path(args.out)
    skills = json.loads((out_dir / "skills.json").read_text(encoding="utf-8"))
    html = Path(args.html).read_text(encoding="utf-8") if args.html else fetch_page_html()
    links = parse_links(html)
    print(f"skill links found on the page: {len(links)} ({len({i for i, _ in links})} distinct ids)")

    owners = game8_unique_owners(SKILL_MD.read_text(encoding="utf-8")) if SKILL_MD.is_file() else {}
    target = out_dir / "skill_aliases.json"
    previous = json.loads(target.read_text(encoding="utf-8")) if target.is_file() else None
    doc = build(links, skills, owners, previous)
    n_ids = sum(len(v) for v in doc["names"].values())
    print(f"names: {len(doc['names'])} ({n_ids} ids)   unmodelled: {len(doc['unmodelled'])}   "
          f"unique owners: {len(doc['unique_owner'])} of {len(owners)} Game8 unique skills")

    if len(doc["names"]) < MIN_NAMES:
        print(f"ERROR: only {len(doc['names'])} names (expected at least {MIN_NAMES}); the wiki page layout may have changed. "
              "Nothing written.", file=sys.stderr)
        return 1
    unseen = [n for n in owners if skill_key(n) not in {skill_key(x) for x in doc["names"]}]
    if unseen:
        print(f"note: {len(unseen)} Game8 unique skill names are not on the wiki page or not in skills.json, e.g. {unseen[:5]}")
    if args.dry_run:
        print("dry run: nothing written")
        return 0
    target.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
