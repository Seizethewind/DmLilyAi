"""CareerReview flow with a fake vision provider (no network)."""
import asyncio
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from LilyAiCore.Exceptions.errors import ProviderError
from LilyAiCore.Providers.base import LLMProvider, LLMResponse
from LilyAiCore.Providers.offline import OfflineProvider
from LilyAiMain.MainService.Interaction.Workflows.career_review import CareerReview
from LilyAiMain.MainService.Interaction.messages import ImageAttachment
from test_career_evaluator import falcon_extraction


class FakeVision(LLMProvider):
    def __init__(self, replies):
        self.replies, self.calls = list(replies), []

    async def list_models(self):
        return []

    async def chat(self, messages, **kw):
        self.calls.append((messages, kw))
        r = self.replies.pop(0)
        if isinstance(r, Exception):
            raise r
        return LLMResponse(content=r)


def img(name="a.png"):
    return ImageAttachment(b"\x89PNG fake", "image/png", name)


def run(coro):
    return asyncio.run(coro)


def test_screenshots_are_read_validated_merged_and_judged():
    skills_tab = falcon_extraction("skills")
    career_tab = falcon_extraction("career_info")
    career_tab["skills"] = []
    provider = FakeVision(["<think>hmm</think>" + json.dumps(skills_tab), json.dumps(career_tab)])
    out = run(CareerReview(provider, "test-vision").review([img("1.png"), img("2.png")], "is she good for long?"))
    assert len(out) == 1
    text = out[0].text
    assert "Smart Falcon" in text and "Long Front Runner on Turf" in text
    assert "Mile Front Runner" not in text  # the caption asked about Long only
    # the vision call must be exact-model, JSON, deterministic, and carry the image as a data URI
    msgs, kw = provider.calls[0]
    assert kw["model"] == "test-vision" and kw["fallback"] is False and kw["json_mode"] and kw["temperature"] == 0
    parts = msgs[0]["content"]
    assert parts[1]["type"] == "image_url" and parts[1]["image_url"]["url"].startswith("data:image/png;base64,")


def test_non_trainee_image_gets_a_helpful_reply():
    provider = FakeVision([json.dumps({"is_trainee_details_screen": False})])
    out = run(CareerReview(provider, "m").review([img()], ""))
    assert "couldn't find a trainee details screen" in out[0].text


def test_garbage_reply_is_not_trusted():
    provider = FakeVision(["I think this is a horse"])
    out = run(CareerReview(provider, "m").review([img()], ""))
    assert "couldn't find a trainee details screen" in out[0].text


def test_provider_failure_says_vision_is_unavailable():
    provider = FakeVision([ProviderError("model not found")])
    out = run(CareerReview(provider, "m").review([img()], ""))
    assert "can't read screenshots right now" in out[0].text


def test_one_failed_screenshot_does_not_sink_the_rest():
    provider = FakeVision([ProviderError("boom"), json.dumps(falcon_extraction())])
    out = run(CareerReview(provider, "m").review([img("bad.png"), img("good.png")], ""))
    assert "Smart Falcon" in out[0].text and "1 screenshot(s) couldn't be read" in out[0].text


def test_offline_provider_never_pretends_to_see():
    out = run(CareerReview(OfflineProvider(), "m").review([img()], ""))
    assert "can't read screenshots right now" in out[0].text


def test_extra_screenshots_are_capped():
    provider = FakeVision([json.dumps(falcon_extraction())] * 6)
    out = run(CareerReview(provider, "m").review([img(f"{i}.png") for i in range(9)], ""))
    assert len(provider.calls) == 6 and "first 6 screenshots" in out[0].text
