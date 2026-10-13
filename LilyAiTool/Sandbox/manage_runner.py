"""Runs Manage Mode's fan analytics in a PandaStack sandbox, with a local fallback.

Same pattern as sandbox_runner.run_calc(): a FIXED script (sandbox_scripts/manage_calcs.py) is uploaded to a throwaway
microVM together with the parameters. The model only supplies parameters, never code. Key rotation, the per-key hourly cap,
the two-sandbox limit, the result cache and the always-kill cleanup all come from sandbox_runner._execute, so there is
still exactly one place that talks to PandaStack.

If the sandbox can't be used (no key, SDK missing, every key rate limited, hourly cap reached, service down) the SAME script
runs in-process instead, so a quota question never fails just because PandaStack is unavailable. A genuine script error
(a bad parameter) is raised either way.
"""
from __future__ import annotations

import asyncio
import importlib.util
import json
from functools import lru_cache
from typing import Any, Callable

from LilyAiCore.Logging.logger import get_logger
from LilyAiTool.Sandbox.sandbox_runner import SCRIPT_DIR, SandboxError, _execute

log = get_logger("gamespace.manage")

MANAGE_SCRIPT = "manage_calcs.py"


@lru_cache(maxsize=1)
def _local_module():
    spec = importlib.util.spec_from_file_location("manage_calcs", SCRIPT_DIR / MANAGE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_local(params: dict[str, Any]) -> str:
    """The same script, in this process. Raises SandboxError with the script's own message on a bad parameter."""
    result = _local_module().run(params)
    if not result.get("ok"):
        raise SandboxError(str(result.get("error") or "The operation failed."))
    return str(result.get("text") or "")


def run_manage(params: dict[str, Any], *, sandbox_factory: Callable[..., Any] | None = None) -> tuple[str, bool]:
    """Returns (text, ran_in_sandbox). Blocking: use run_manage_async() from the bot's event loop."""
    payload = json.dumps(params, sort_keys=True, ensure_ascii=False)
    try:
        return _execute(MANAGE_SCRIPT, "", payload, sandbox_factory), True
    except SandboxError as e:
        log.info("manage analytics: sandbox unavailable or refused (%s); running the same script locally", e)
    return run_local(params), False


async def run_manage_async(params: dict[str, Any], **kw: Any) -> tuple[str, bool]:
    return await asyncio.to_thread(run_manage, params, **kw)
