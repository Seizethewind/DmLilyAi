"""Router provider tests (no network, no API keys): request shape, no model fallback, settings defaults, provider choice.

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:  # allow running the tests without httpx installed
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.Exceptions.errors import ConfigError, ProviderError  # noqa: E402
from LilyAiCore.Providers.Groq.client import GroqProvider  # noqa: E402
from LilyAiCore.Providers.offline import OfflineProvider  # noqa: E402
from LilyAiCore.Providers.Router.client import RouterProvider  # noqa: E402

_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


class FakeResponse:
    def __init__(self, status_code=200, payload=None, text=""):
        self.status_code, self._payload, self.text, self.headers = status_code, payload or {}, text, {}

    def json(self):
        return self._payload


OK_BODY = {"choices": [{"message": {"content": "hello from the router"}}], "model": "groq/llama", "usage": {"total_tokens": 3}}


class FakeClient:
    """Stands in for httpx.AsyncClient and records every request."""

    instances: list["FakeClient"] = []
    reply = FakeResponse(200, OK_BODY)

    def __init__(self, **kwargs):
        self.kwargs, self.posts = kwargs, []
        FakeClient.instances.append(self)

    async def post(self, path, json=None, headers=None):
        self.posts.append({"path": path, "json": json, "headers": headers})
        return FakeClient.reply

    async def aclose(self):
        return None


FAKE_HTTPX = types.SimpleNamespace(AsyncClient=FakeClient, HTTPError=Exception)
MESSAGES = [{"role": "user", "content": "hi"}]


class RouterProviderTests(unittest.TestCase):
    def setUp(self):
        FakeClient.instances.clear()
        FakeClient.reply = FakeResponse(200, OK_BODY)
        patcher = mock.patch("LilyAiCore.Providers.Groq.client.httpx", FAKE_HTTPX)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_request_is_plain_openai_shaped(self):
        p = RouterProvider("rk-1", "https://router.example/v1/")
        out = run(p.chat(MESSAGES, max_tokens=50))
        client = FakeClient.instances[0]
        self.assertEqual(client.kwargs["base_url"], "https://router.example/v1")
        sent = client.posts[0]
        self.assertEqual(sent["path"], "/chat/completions")
        self.assertEqual(sent["headers"], {"Authorization": "Bearer rk-1"})
        self.assertEqual(sent["json"]["model"], "auto:fast")
        self.assertEqual(sent["json"]["max_tokens"], 50)
        self.assertNotIn("max_completion_tokens", sent["json"])
        self.assertEqual(out.content, "hello from the router")

    def test_selector_passes_through(self):
        run(RouterProvider("rk", "https://router.example/v1").chat(MESSAGES, model="auto:smart"))
        self.assertEqual(FakeClient.instances[0].posts[0]["json"]["model"], "auto:smart")

    def test_groq_still_sends_its_own_token_field(self):
        run(GroqProvider("gk").chat(MESSAGES, max_tokens=7, fallback=False))
        self.assertEqual(FakeClient.instances[0].posts[0]["json"]["max_completion_tokens"], 7)

    def test_failure_does_not_fall_back_to_other_model_ids(self):
        FakeClient.reply = FakeResponse(400, text="bad request")
        p = RouterProvider("rk", "https://router.example/v1")
        with self.assertRaises(ProviderError):
            run(p.chat(MESSAGES, fallback=True))
        self.assertEqual(len(FakeClient.instances[0].posts), 1)

    def test_missing_settings_say_which_one(self):
        with self.assertRaisesRegex(ConfigError, "ROUTER_API_KEY"):
            RouterProvider([], "https://router.example/v1")
        with self.assertRaisesRegex(ConfigError, "ROUTER_BASE_URL"):
            RouterProvider("rk", "  ")

    def test_only_groq_is_scanned_for_models(self):
        self.assertFalse(RouterProvider.scans_models)
        self.assertFalse(OfflineProvider.scans_models)
        self.assertTrue(GroqProvider.scans_models)


class SettingsAndChoiceTests(unittest.TestCase):
    ROUTER_ENV = {"ROUTER_BASE_URL": "https://router.example/v1", "ROUTER_API_KEY": "rk-1"}

    def env(self, **extra):
        tmp = tempfile.mkdtemp()
        patcher = mock.patch.dict(os.environ, {"LILYAI_DATA_DIR": tmp, "GROQ_API_KEY": "", **extra})
        patcher.start()
        self.addCleanup(patcher.stop)
        for name in {"LILYAI_CHAT_MODEL", "LILYAI_REASONING_MODEL", "ROUTER_BASE_URL", "ROUTER_API_KEY"} - set(extra):
            os.environ.pop(name, None)
        return tmp

    def test_router_defaults_are_selectors(self):
        self.env(**self.ROUTER_ENV)
        s = load_settings()
        self.assertTrue(s.via_router)
        self.assertEqual((s.chat_model, s.reasoning_model), ("auto:fast", "auto:smart"))

    def test_explicit_models_win(self):
        self.env(**self.ROUTER_ENV, LILYAI_CHAT_MODEL="auto:coding")
        self.assertEqual(load_settings().chat_model, "auto:coding")

    def test_url_without_key_is_not_the_router(self):
        self.env(ROUTER_BASE_URL="https://router.example/v1")
        s = load_settings()
        self.assertFalse(s.via_router)
        self.assertEqual(s.chat_model, "openai/gpt-oss-20b")

    def test_build_app_picks_router_then_groq_then_offline(self):
        from LilyAiMain.MainService.bootstrap import build_app

        with mock.patch("LilyAiCore.Providers.Groq.client.httpx", FAKE_HTTPX):
            self.env(**self.ROUTER_ENV, GROQ_API_KEY="gk")
            app = build_app(load_settings(), search_provider=object())
            self.assertIsInstance(app.provider, RouterProvider)
            self.assertEqual(app.pool.all(), [])

            self.env(GROQ_API_KEY="gk")
            app = build_app(load_settings(), search_provider=object())
            self.assertIs(type(app.provider), GroqProvider)
            self.assertTrue(app.pool.all())

        self.env()
        app = build_app(load_settings(), search_provider=object())
        self.assertIsInstance(app.provider, OfflineProvider)


if __name__ == "__main__":
    unittest.main()
