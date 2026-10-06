"""Simulator Mode screenshots: read each image with the vision model, keep the veteran screens, save them for this user.

Same shape as career_review.CareerReview: the vision model only transcribes (VeteranIntake.INTAKE_PROMPT), code validates
(VeteranReader.normalize_veteran) and merges screenshots of the same veteran, and the reply is written by code, not the model.
Uses the same vision model setting as the career review (LILYAI_VISION_MODEL) and MAX_IMAGES.
"""
from __future__ import annotations

import base64

from LilyAiCore.Exceptions.errors import ProviderError
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiCore.Providers.offline import OfflineProvider
from LilyAiMain.MainService.Interaction.messages import ImageAttachment, OutgoingMessage
from LilyAiMain.MainService.Interaction.Workflows.career_review import MAX_IMAGES, _NO_VISION, _vision_model
from LilyAiMemory.Veteran.veteran_store import VeteranLimitError, VeteranStore

log = get_logger("veteran_intake")

_NOT_VETERAN = ("I couldn't find a veteran details screen in that. Send the \"Umamusume Details\" screen of a finished "
                "trainee (the skills tab; two or three screenshots if the list scrolls).")


class VeteranIntakeFlow:
    def __init__(self, provider: LLMProvider, store: VeteranStore, vision_model: str | None = None):
        self.provider, self.store = provider, store
        self.vision_model = vision_model or _vision_model()

    async def _ask(self, image: ImageAttachment, prompt: str) -> str:
        data_uri = f"data:{image.mime};base64,{base64.b64encode(image.data).decode('ascii')}"
        messages = [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": data_uri}},
        ]}]
        # fallback=False: a text-only fallback model cannot see the image and would invent a reading.
        response = await self.provider.chat(
            messages, model=self.vision_model, temperature=0, max_tokens=3000, json_mode=True, fallback=False)
        return response.content or ""

    async def intake(self, user_id: str, images: list[ImageAttachment], caption: str = "") -> list[OutgoingMessage]:
        # Imported here so the bot starts (and Chat Mode works) even if the Simulation folder has a problem.
        from LilyAiGameSpace.Umamusume.Simulation import sim_service

        if isinstance(self.provider, OfflineProvider):
            return [OutgoingMessage(_NO_VISION, kind="system")]
        notes: list[str] = []
        if len(images) > MAX_IMAGES:
            notes.append(f"I only looked at the first {MAX_IMAGES} screenshots.")
        failures = 0

        async def ask(image, prompt):
            nonlocal failures
            try:
                return await self._ask(image, prompt)
            except ProviderError as e:
                log.warning("vision call failed for %s: %s", image.name, e)
                failures += 1
                return ""   # parses as "not a veteran", so the other screenshots still count

        outcome = await sim_service.intake_images(images[:MAX_IMAGES], ask)
        if failures and failures == len(images[:MAX_IMAGES]):
            return [OutgoingMessage(_NO_VISION, kind="system")]
        if not outcome["is_veteran_upload"]:
            return [OutgoingMessage(_NOT_VETERAN, kind="system")]

        lines = [sim_service.format_intake_reply(outcome)]
        for vet in outcome["veterans"]:
            try:
                vet_id, status = self.store.save(user_id, vet)
            except VeteranLimitError as e:
                lines.append(str(e))
                continue
            lines.append(f"Saved as veteran #{vet_id} ({status}). Ask me to simulate it, e.g. "
                         f"\"simulate #{vet_id} on Tokyo 2400 turf\".")
        if failures:
            notes.append(f"{failures} screenshot(s) couldn't be read, so this is based on the rest.")
        return [OutgoingMessage("\n".join([*lines, *notes]), meta={"model": self.vision_model, "tools": ["veteran_intake"]})]
