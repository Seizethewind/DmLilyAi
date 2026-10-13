"""Runs model-written code in a throwaway PandaStack microVM (the Chat Mode VM tool).

Unlike sandbox_runner.py, which only ever runs FIXED scripts and can fall back to running them inside the bot, this
module runs code the chat model wrote. So it has one hard rule: it only ever runs inside a real microVM. There is no
local fallback, ever. If the sandbox can't be used the call fails with a plain message and nothing runs in the bot.

It reuses sandbox_runner's key pool (rotation, cooldowns, per-key hourly cap), its two-at-once slot limit and its
key-failure classifier, so code runs and the game calculators share one budget of PandaStack credit.
Every run boots a fresh VM and kills it afterwards, so nothing is kept between runs. Results are never cached.

Env:
    PANDASTACK_API_KEY             shared with sandbox_runner (one key, or several comma-separated)
    PANDASTACK_TEMPLATE            shared with sandbox_runner (default "code-interpreter")
    LILYAI_VM_MAX_RUNS_PER_HOUR    default 10: a cap on code runs for the whole bot, on top of the per-key cap
"""
from __future__ import annotations

import asyncio
import os
import threading
from typing import Any, Callable

from LilyAiCore.Logging.logger import get_logger
from LilyAiTool.Sandbox import sandbox_runner as sr
from LilyAiTool.Sandbox.sandbox_runner import SandboxError

log = get_logger("gamespace.vm")

LANGUAGES: dict[str, tuple[str, str]] = {"python": ("main.py", "python3"), "bash": ("main.sh", "bash")}
MAX_CODE_CHARS = 20_000
DEFAULT_TIMEOUT_S = 30
MAX_TIMEOUT_S = 60
MAX_STREAM_CHARS = 1_800      # per stream (stdout, stderr); the tool executor caps a whole reply at 4,000 characters

_guard: "sr._RateGuard | None" = None
_guard_lock = threading.Lock()


def max_runs_per_hour() -> int:
    try:
        return max(1, int(os.getenv("LILYAI_VM_MAX_RUNS_PER_HOUR", "10")))
    except ValueError:
        return 10


def _allow_run() -> bool:
    global _guard
    with _guard_lock:
        if _guard is None:
            _guard = sr._RateGuard(max_runs_per_hour())
        guard = _guard
    return guard.allow()


def is_available() -> bool:
    """True when a real sandbox can be used (key set and SDK installed). The local fallback never counts."""
    return sr.is_configured()


def _clip(text: str) -> str:
    """Keep the start and the end: a traceback's useful line is at the bottom, a program's header at the top."""
    if len(text) <= MAX_STREAM_CHARS:
        return text
    half = MAX_STREAM_CHARS // 2
    return f"{text[:half]}\n... [{len(text) - MAX_STREAM_CHARS:,} characters cut] ...\n{text[-half:]}"


def _format(res: Any) -> str:
    stdout = (getattr(res, "stdout", "") or "").rstrip()
    stderr = (getattr(res, "stderr", "") or "").rstrip()
    code = getattr(res, "exit_code", 0)
    lines = [f"exit code: {0 if code is None else code}"]
    lines.append(f"stdout:\n{_clip(stdout)}" if stdout else "stdout: (empty)")
    if stderr:
        lines.append(f"stderr:\n{_clip(stderr)}")
    return "\n".join(lines)


def _timed_out(exc: Exception) -> bool:
    return "timeout" in type(exc).__name__.lower() or "timed out" in str(exc).lower() or "timeout" in str(exc).lower()


def run_code(language: str | None, code: str, *, timeout_s: int | None = None,
             sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Blocking. Run `code` in a fresh microVM and return "exit code / stdout / stderr" as text.

    A program that fails (non-zero exit) is a normal result: its stderr is returned so the model can fix the code.
    Raises SandboxError when the VM can't be used at all (no key, rate limited, hourly cap, bad input, timed out).
    """
    language = (language or "python").strip().lower()
    spec = LANGUAGES.get(language)
    if spec is None:
        raise SandboxError(f"language must be one of: {', '.join(LANGUAGES)}.")
    if not code or not code.strip():
        raise SandboxError("There is no code to run.")
    if len(code) > MAX_CODE_CHARS:
        raise SandboxError(f"That code is too long to run ({len(code):,} characters; the limit is {MAX_CODE_CHARS:,}).")
    timeout = DEFAULT_TIMEOUT_S if timeout_s is None else max(1, min(int(timeout_s), MAX_TIMEOUT_S))

    keys = sr.load_keys()
    if sandbox_factory is None:
        if not (keys and sr.sdk_installed()):
            raise SandboxError("The VM isn't set up (PANDASTACK_API_KEY or the pandastack package is missing).")
        sandbox_factory = sr._default_factory
    elif not keys:
        keys = ["test-key"]          # injected factories (tests) don't need a real key
    if not _allow_run():
        raise SandboxError("VM run limit reached for this hour. Try again later.")
    if not sr._slots.acquire(timeout=10):
        raise SandboxError("The VM is busy right now. Try again in a moment.")

    fname, runner = spec
    template = os.getenv("PANDASTACK_TEMPLATE", "code-interpreter")
    key_failed = 0
    try:
        for key in sr._pool.order(keys):
            if not sr._pool.allow(key):
                continue
            sbx = None
            started = False
            try:
                sbx = sandbox_factory(template, sr.SANDBOX_TTL_S, key)
                sbx.filesystem.write(f"/workspace/{fname}", code)
                started = True
                res = sbx.exec(f"{runner} /workspace/{fname}", timeout_seconds=timeout)
                return _format(res)
            except SandboxError:
                raise
            except Exception as e:
                rest = sr._classify(e)
                if rest is None:
                    if started and _timed_out(e):
                        raise SandboxError(f"The code ran past the {timeout}s limit and was stopped.")
                    log.warning("vm call failed: %s: %s", type(e).__name__, str(e)[:200])
                    raise SandboxError("Couldn't reach the VM service. Try again in a minute.")
                key_failed += 1
                sr._pool.cool(key, rest)
                log.warning("pandastack key %s resting %ds (%s); trying the next key", sr._kid(key), rest, type(e).__name__)
            finally:
                if sbx is not None:
                    try:
                        sbx.kill()
                    except Exception:
                        pass   # the TTL reaps it
        if key_failed:
            raise SandboxError("Every PandaStack key is rate limited or out of credit right now. Try again later.")
        raise SandboxError("VM limit reached for this hour. Try again later.")
    finally:
        sr._slots.release()


async def run_code_async(language: str | None, code: str, **kw: Any) -> str:
    return await asyncio.to_thread(run_code, language, code, **kw)
