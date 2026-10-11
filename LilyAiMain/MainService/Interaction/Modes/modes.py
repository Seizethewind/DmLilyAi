"""Request modes: Chat (default), Manage, Analyst and Simulator.

Why this exists: with every tool and every game doc in play on every turn, Lily kept answering from the docs.
A mode narrows what one turn can use:

    Chat       web search + everyday tools, and the optional VM (run_code). No game docs. (default)
    Manage     uma.moe workflow: fan gain, leaderboard, circle standing, trainer link, reminders.
    Analyst    the Umamusume docs: doc search/read, table maths, calculators, affinity, your collection.
    Simulator  veterans and the race simulator.

The mode is kept in the user's session (LilyAiMemory SessionMemory), so it resets to Chat after the session idles out.
The user switches by typing "mode" (the four buttons appear) or a phrase such as "simulator mode".
Tool categories come from LilyAiTool (ToolSpec.category). Keep the example phrases in
LilyAiContext/CapabilityContext/capabilities.py (DM_ACTIONS) matching the patterns here.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from LilyAiMain.MainService.Interaction.messages import MenuItem

DEFAULT_MODE = "chat"


@dataclass(frozen=True)
class Mode:
    key: str
    label: str
    blurb: str
    categories: frozenset[str]   # tool categories this mode may use
    game_docs: bool = False      # inject matching game-doc passages into the prompt


MODES: dict[str, Mode] = {
    "chat": Mode(
        "chat", "Chat Mode", "everyday chat with web search",
        # "vm" is the optional run_code tool: it is only registered when a PandaStack key and an allowed user are set.
        frozenset({"web", "utility", "discord", "umapyoi", "vm"}),
    ),
    "manage": Mode(
        "manage", "Manage Mode", "leaderboard, fan gain, uma.moe and your carat balance",
        frozenset({"umamoe", "utility", "discord", "carats"}),
    ),
    "analyst": Mode(
        "analyst", "Analyst Mode", "answers from the game data docs (guides, skills, cards, tables, calculators)",
        frozenset({"gamespace", "collection", "utility"}), game_docs=True,
    ),
    "simulator": Mode(
        "simulator", "Simulator Mode", "simulating a veteran on a race course",
        frozenset({"simulator", "utility"}),
    ),
}

_ALIASES = {
    "chat": "chat",
    "manage": "manage", "management": "manage",
    "analyst": "analyst", "analysis": "analyst", "analyze": "analyst", "analyse": "analyst",
    "simulator": "simulator", "simulation": "simulator", "sim": "simulator",
}
_KEYS = "|".join(sorted(_ALIASES, key=len, reverse=True))

# "simulator mode", "switch to manage mode", "please go to the analyst mode"
SWITCH_RE = re.compile(
    r"^\s*(?:(?:please\s+)?(?:(?:switch|change|go|set)(?:\s+(?:me|it))?\s+(?:to|into)|use|enter)\s+)?(?:the\s+)?"
    rf"({_KEYS})\s+mode\s*[.!]*\s*$",
    re.I,
)
# "mode", "modes", "switch mode", "which mode?"
MENU_RE = re.compile(
    r"^\s*(?:modes?|(?:show|open|list|change|switch)\s+(?:the\s+)?modes?|what\s+modes\s+(?:are\s+there|do\s+you\s+have)|which\s+mode)\s*[?.!]*\s*$",
    re.I,
)
CURRENT_RE = re.compile(r"^\s*(?:what|which)\s+mode\s+(?:am\s+i\s+in|is\s+this)\s*[?.!]*\s*$", re.I)

# Words that suggest another mode would serve the message better (used for a one-time tip after a chat reply).
_SIM_HINT = re.compile(r"\b(?:simulat\w*|veterans?|time\s+trial)\b", re.I)
_MANAGE_HINT = re.compile(r"\b(?:fan\s*gain|leaderboard|quota|circle\s+(?:rank|standing)|uma\.?moe|carats?)\b", re.I)


def mode_of(session) -> Mode:
    return MODES.get(session.data.get("mode", DEFAULT_MODE), MODES[DEFAULT_MODE])


def mode_menu() -> list[MenuItem]:
    return [MenuItem(m.label, f"switch to {m.key} mode") for m in MODES.values()]


def menu_text(current: Mode) -> str:
    lines = [f"You're in **{current.label}**. Pick a mode:"]
    lines += [f"- **{m.label}**: {m.blurb}" for m in MODES.values()]
    return "\n".join(lines)


_WELCOME = {
    "chat": "Back to everyday chat. I'll search the web when it helps.",
    "manage": "Ask about fan gain, the leaderboard, circle standing, your Trainer ID or reminders. Tell me your carat amount (e.g. \"I have 20k carats\") and I'll track your income.",
    "analyst": "Ask about characters, skills, support cards, race lists or guides, or send a trainee screenshot for a review.",
    "simulator": ("Send screenshots of a veteran (the Umamusume Details screen, skills tab) to save it, then ask me to "
                  "simulate it on a course, e.g. \"simulate Oguri Cap on Tokyo 2400 turf\"."),
}


def switch_text(mode: Mode) -> str:
    return f"Switched to **{mode.label}**. {_WELCOME[mode.key]}"


def match_switch(text: str) -> str | None:
    """The mode key if `text` is a request to switch modes, else None."""
    m = SWITCH_RE.match(text)
    return _ALIASES[m.group(1).lower()] if m else None


def suggest_mode(text: str, current: Mode, game_doc_hit: bool) -> Mode | None:
    """A mode that would handle `text` better than `current`, or None. Only a hint: the user decides."""
    if current.key != "simulator" and _SIM_HINT.search(text):
        return MODES["simulator"]
    if current.key != "manage" and _MANAGE_HINT.search(text):
        return MODES["manage"]
    # Only from Chat Mode, where the docs are switched off. In Simulator or Manage Mode a character or skill name is
    # part of the request ("simulate Oguri Cap on Tokyo 2400"), not a sign the user wants the docs.
    if current.key == "chat" and game_doc_hit:
        return MODES["analyst"]
    return None


def prompt_note(mode: Mode) -> str:
    """One paragraph for the system prompt: what this turn can and can't do, and how to point the user elsewhere."""
    others = {k: m for k, m in MODES.items() if k != mode.key}
    switch = "; ".join(f'"{k} mode" for {m.blurb}' for k, m in others.items())
    return (
        f"Current mode: {mode.label} ({mode.blurb}). Only the tools listed under \"Tools available\" work in this mode. "
        "If the user asks for something another mode handles, don't say you can't: tell them the exact words to switch "
        f"({switch}) and that the buttons appear when they type \"mode\"."
    )
