"""Offline provider used when no model provider is configured, so the app, DM Simulator and tests still run."""
from LilyAiCore.Providers.base import LLMProvider, LLMResponse


class OfflineProvider(LLMProvider):
    scans_models = False

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        last = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
        if json_mode:
            return LLMResponse(content='{"facts": []}', model="offline")
        return LLMResponse(
            content=f"(offline mode - set ROUTER_BASE_URL and ROUTER_API_KEY for real replies) You said: {last[:300]}",
            model="offline",
        )

    async def list_models(self) -> list[str]:
        return []
