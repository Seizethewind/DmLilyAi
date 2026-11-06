"""Self-hosted router provider (FreeLLMAPI / 9Router). Pure transport: no business logic.

The router speaks the OpenAI chat format, so this reuses the Groq transport (retries, key rotation). Two differences:
the model field is a router selector (`auto`, `auto:fast`, `auto:smart`, `auto:<profile>`) or a model id, and the
router does the model choice and the failover itself, so other model ids are never tried from here.
"""
from LilyAiCore.Config.models import ModelPool
from LilyAiCore.Exceptions.errors import ConfigError
from LilyAiCore.Providers.base import LLMResponse
from LilyAiCore.Providers.Groq.client import GroqProvider


class RouterProvider(GroqProvider):
    max_tokens_field = "max_tokens"
    scans_models = False  # the router owns the model list; probing it on a schedule would only spend free-tier quota

    def __init__(
        self,
        api_keys: list[str] | str,
        base_url: str,
        default_model: str = "auto:fast",
        pool: ModelPool | None = None,
        timeout: float = 120.0,  # free-tier models behind a router can be slow
        max_retries: int = 2,
    ):
        keys = [api_keys] if isinstance(api_keys, str) else list(api_keys)
        if not base_url.strip():
            raise ConfigError("ROUTER_BASE_URL is not set")
        if not keys:
            raise ConfigError("ROUTER_API_KEY is not set")
        super().__init__(keys, base_url.strip(), default_model, pool or ModelPool(()), timeout, max_retries)

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True) -> LLMResponse:
        # `fallback` is accepted for the interface and ignored: the router already fails over between its providers.
        return await super().chat(
            messages, model=model, tools=tools, temperature=temperature, max_tokens=max_tokens,
            json_mode=json_mode, fallback=False,
        )
