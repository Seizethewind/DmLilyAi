"""Review of post-career trainee screenshots.

Flow: each screenshot -> vision model transcribes it into JSON -> code validates it (TraineeSheet) -> the screenshots of
one trainee are merged -> code judges the result against the guide docs (CareerEvaluator). The model never writes the
verdict, and nothing from the screenshots is stored.

Set LILYAI_VISION_MODEL to change the vision model (Groq's vision lineup changes often) and LILYAI_STAT_CAP for the
default stat cap. The user can override the cap in the caption ("cap 1200").
"""
from __future__ import annotations

import base64
import os

from LilyAiCore.Exceptions.errors import ProviderError
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiCore.Providers.offline import OfflineProvider
from LilyAiGameSpace.Umamusume.CareerEvaluator import DEFAULT_CAP, evaluate, parse_goal, render_report
from LilyAiGameSpace.Umamusume.TraineeSheet import Sheet, extract_json, merge_sheets, sheet_from_extraction
from LilyAiMain.MainService.Interaction.messages import ImageAttachment, OutgoingMessage

log = get_logger("career_review")

DEFAULT_VISION_MODEL = "qwen/qwen3.8-27b"  # the model Groq's vision docs list (Sep 2026); override with LILYAI_VISION_MODEL
MAX_IMAGES = 6

_PROMPT = """You are reading ONE screenshot from the game Umamusume: Pretty Derby. Transcribe it. Reply with ONLY a JSON object, no other text.

The screen of interest is titled "Umamusume Details". Return:
{
  "is_trainee_details_screen": true or false,
  "active_tab": "skills" | "inspiration" | "career_info",
  "trainee": {"name": "e.g. Smart Falcon", "outfit": "the text in brackets above the name, e.g. LOVE☆4EVER", "rating": the number under the portrait},
  "stats": {"speed": int, "stamina": int, "power": int, "guts": int, "wit": int},
  "aptitudes": {"turf": "S-G", "dirt": "S-G", "sprint": "S-G", "mile": "S-G", "medium": "S-G", "long": "S-G", "front": "S-G", "pace": "S-G", "late": "S-G", "end": "S-G"},
  "skills": [{"name": "...", "rarity": "white|gold|unique|negative", "icon": "recovery|speed|acceleration|green|debuff|other"}],
  "uncertain": ["short notes about anything you could not read clearly"]
}

Rules:
- is_trainee_details_screen is true only for the Umamusume Details screen that shows the five stats. Otherwise return {"is_trainee_details_screen": false}.
- active_tab is the one of the three tabs under the aptitude table that is highlighted green.
- stats are the plain numbers next to the Speed / Stamina / Power / Guts / Wit labels. Do NOT return the letter-rank icons (B+, SS, UB3...).
- aptitudes are single letters S, A, B, C, D, E, F or G. If a letter is not clearly legible use null. Do not guess.
- skills: ONLY when active_tab is "skills". List every skill row that is visible, top to bottom, left column then right column per row. Keep the circle after a name (a single circle or a double circle). Put "Lvl 5" style text on the unique skill's name. rarity comes from the row colour (grey/lavender = white, yellow = gold, rainbow = unique, purple = negative). icon comes from the icon (blue sparkle = recovery, orange = speed/acceleration/other, green = green skill). If another tab is active, return "skills": [].
- Never invent values. Use null for anything you cannot read."""

_NO_VISION = "I can't read screenshots right now (no vision model is available on my side). Tell me the stats in words and I'll still help."
_NOT_TRAINEE = ("I couldn't find a trainee details screen in that. Send the \"Umamusume Details\" screen "
                "(the Skills tab, scrolled to the end if the list is long) and I'll review the build.")


def _vision_model() -> str:
    return os.getenv("LILYAI_VISION_MODEL", "").strip() or DEFAULT_VISION_MODEL


def _default_cap() -> int:
    raw = os.getenv("LILYAI_STAT_CAP", "").strip()
    return int(raw) if raw.isdigit() and 1000 <= int(raw) <= 3000 else DEFAULT_CAP


class CareerReview:
    def __init__(self, provider: LLMProvider, vision_model: str | None = None):
        self.provider = provider
        self.vision_model = vision_model or _vision_model()

    async def _read_one(self, image: ImageAttachment) -> Sheet | None:
        data_uri = f"data:{image.mime};base64,{base64.b64encode(image.data).decode('ascii')}"
        messages = [{"role": "user", "content": [
            {"type": "text", "text": _PROMPT},
            {"type": "image_url", "image_url": {"url": data_uri}},
        ]}]
        # fallback=False: a text-only fallback model cannot see the image and would invent a reading.
        response = await self.provider.chat(
            messages, model=self.vision_model, temperature=0, max_tokens=3000, json_mode=True, fallback=False,
        )
        data = extract_json(response.content)
        if data is None:
            log.warning("vision reply for %s had no JSON object", image.name)
            return None
        return sheet_from_extraction(data)

    async def review(self, images: list[ImageAttachment], caption: str = "") -> list[OutgoingMessage]:
        if isinstance(self.provider, OfflineProvider):
            return [OutgoingMessage(_NO_VISION, kind="system")]
        notes: list[str] = []
        sheets: list[Sheet] = []
        if len(images) > MAX_IMAGES:
            notes.append(f"I only looked at the first {MAX_IMAGES} screenshots.")
        failed = 0
        for image in images[:MAX_IMAGES]:
            try:
                sheet = await self._read_one(image)
            except ProviderError as e:
                log.warning("vision call failed for %s: %s", image.name, e)
                failed += 1
                continue
            if sheet is not None and not sheet.is_empty:
                sheets.append(sheet)
        if not sheets:
            if failed == len(images[:MAX_IMAGES]):
                return [OutgoingMessage(_NO_VISION, kind="system")]
            return [OutgoingMessage(_NOT_TRAINEE, kind="system")]
        if failed:
            notes.append(f"{failed} screenshot(s) couldn't be read, so the review is based on the rest.")

        merged = merge_sheets(sheets)
        merged.notes += notes
        goal, cap = parse_goal(caption)
        report = evaluate(merged, cap=cap or _default_cap(), goal=goal)
        return [OutgoingMessage(render_report(report), meta={"model": self.vision_model, "tools": ["career_review"]})]
