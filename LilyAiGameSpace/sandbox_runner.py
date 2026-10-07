"""Runs fixed table operations on Umamusume docs inside a PandaStack sandbox, with a local fallback.

Flow: the chat model picks a doc + operation -> this module pulls the RAW section text from the
engine (not the 2,000-char clipped passages the guide builder uses) -> uploads it with a fixed script
(sandbox_scripts/docs_table_ops.py) to a throwaway microVM -> returns the printed result.
Calculators work the same way with sandbox_scripts/game_calcs.py, but need no doc text: the rules are in the script.

The model only supplies parameters. It never supplies code. Everything blocking is wrapped by
run_table_op_async() so the bot's event loop is never stalled.

If the sandbox can't be used (no key, SDK missing, every key rate limited, hourly cap reached, service down) the SAME
fixed script runs in-process instead (see run_local), so a calculation never fails just because PandaStack is
unavailable. A genuine script error (a bad parameter) is raised either way. manage_runner does the same for Manage Mode.

Env:
    PANDASTACK_API_KEY             one key, or up to 6 comma-separated (e.g. psk_a,psk_b,psk_c), like GROQ_API_KEY.
                                   Runs are spread evenly across the keys; a key that is rate limited, out of credit
                                   or rejected is skipped for a while and the next key is tried automatically.
    PANDASTACK_TEMPLATE            default "code-interpreter"
    PANDASTACK_MAX_RUNS_PER_HOUR   default 30 PER KEY (cost guard for each key's free-tier credit)
    LILYAI_SANDBOX_LOCAL_FALLBACK  default on; 0/false/no/off turns the in-process fallback off
    LILYAI_SANDBOX_LOCAL_MAX_CHARS default 8,000,000; a local run is refused above this many input characters
"""
from __future__ import annotations

import asyncio
import hashlib
import importlib.util
import json
import os
import threading
import time
from collections import OrderedDict, deque
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from LilyAiCore.Logging.logger import get_logger
from LilyAiGameSpace.UmamusumeGameSpaceEngine import UmamusumeGameSpaceEngine, get_engine

log = get_logger("gamespace.sandbox")

SCRIPT_DIR = Path(__file__).resolve().parent / "sandbox_scripts"
TABLE_SCRIPT, CALC_SCRIPT, AFFINITY_SCRIPT = "docs_table_ops.py", "game_calcs.py", "affinity_calc.py"
MAX_RAW_CHARS = 400_000          # far below the engine's 2 MB file cap; keeps the upload small
EXEC_TIMEOUT_S = 30
SANDBOX_TTL_S = 120              # backstop: the VM reaps itself if we crash before kill()
CACHE_TTL_S = 600
CACHE_MAX = 64
MAX_KEYS = 6
COOLDOWN_RATE_LIMIT_S = 60        # key hit a rate limit: rest it briefly
COOLDOWN_BAD_KEY_S = 3600         # key rejected or out of credit: rest it for an hour
LOCAL_MAX_CHARS_DEFAULT = 8_000_000   # doc text plus data files a local run may be handed


class SandboxError(Exception):
    """A user-presentable failure (never includes keys or stack traces)."""


class _LocalTooLarge(SandboxError):
    """The input is too big for the in-process fallback (the sandbox's own error is reported instead)."""


def load_keys() -> list[str]:
    """PANDASTACK_API_KEY split on commas, de-duplicated, at most MAX_KEYS (extra keys are ignored)."""
    keys: list[str] = []
    for k in os.getenv("PANDASTACK_API_KEY", "").split(","):
        k = k.strip()
        if k and k not in keys:
            keys.append(k)
    if len(keys) > MAX_KEYS:
        log.warning("PANDASTACK_API_KEY has %d keys; only the first %d are used", len(keys), MAX_KEYS)
    return keys[:MAX_KEYS]


def api_key_set() -> bool:
    return bool(load_keys())


def sdk_installed() -> bool:
    try:
        import pandastack  # noqa: F401
        return True
    except Exception:
        return False


def is_configured() -> bool:
    """True when a real PandaStack sandbox can be used (key set and SDK installed)."""
    return api_key_set() and sdk_installed()


def local_fallback_enabled() -> bool:
    """The same fixed scripts, run inside the bot when the sandbox can't be used. On unless switched off."""
    return os.getenv("LILYAI_SANDBOX_LOCAL_FALLBACK", "1").strip().lower() not in ("0", "false", "no", "off")


def can_run() -> bool:
    """True when the calculators can run at all: a configured sandbox, or the local fallback."""
    return is_configured() or local_fallback_enabled()


def _local_max_chars() -> int:
    try:
        return max(10_000, int(os.getenv("LILYAI_SANDBOX_LOCAL_MAX_CHARS", str(LOCAL_MAX_CHARS_DEFAULT))))
    except ValueError:
        return LOCAL_MAX_CHARS_DEFAULT


# ------------------------------------------------------------------ raw doc text
def raw_section_text(ref: str, section: str | None = None, category: str | None = None,
                     engine: UmamusumeGameSpaceEngine | None = None) -> tuple[str, str, str, str]:
    """Return (doc_id, title, section_path, full_text) with NO clipping. Raises SandboxError if not found."""
    eng = engine or get_engine()
    doc = eng.resolve(ref, category)
    if doc is None:
        similar = eng.suggest(ref)
        hint = f" Did you mean: {', '.join(similar)}?" if similar else ""
        raise SandboxError(f"No doc found for {ref!r}.{hint}")
    secs = doc.visible()

    def render(items) -> str:
        return "\n\n".join(f"{'#' * s.level} {s.heading}\n{s.text}".rstrip() for s in items)

    if section:
        idx = eng._find_section(secs, section)
        if idx is None:
            names = ", ".join(s.path for s in secs if s.level > 1)[:300]
            raise SandboxError(f"No section matching {section!r} in {doc.title}. Sections: {names}")
        text, path = render(eng._subtree(secs, idx)), secs[idx].path
    else:
        text, path = render(secs), ""
    if len(text) > MAX_RAW_CHARS:
        raise SandboxError(f"{doc.title} is too large to process in one go ({len(text):,} chars). Name a section.")
    if not text.strip():
        raise SandboxError(f"That part of {doc.title} is empty.")
    return doc.id, doc.title, path, text


# ------------------------------------------------------------------ guards
class _RateGuard:
    def __init__(self, per_hour: int):
        self.per_hour = per_hour
        self._stamps: deque[float] = deque()
        self._lock = threading.Lock()

    def allow(self) -> bool:
        now = time.monotonic()
        with self._lock:
            while self._stamps and now - self._stamps[0] > 3600:
                self._stamps.popleft()
            if len(self._stamps) >= self.per_hour:
                return False
            self._stamps.append(now)
            return True


def _max_runs() -> int:
    try:
        return max(1, int(os.getenv("PANDASTACK_MAX_RUNS_PER_HOUR", "30")))
    except ValueError:
        return 30


def _kid(key: str) -> str:
    """Short non-reversible id for a key, safe to log. The key itself is never logged."""
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:6]


class _KeyPool:
    """Round-robin over the keys, with a per-key cooldown and a per-key hourly cap."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._next = 0
        self._cool: dict[str, float] = {}
        self._guards: dict[str, _RateGuard] = {}

    def order(self, keys: list[str]) -> list[str]:
        """Keys in the order to try: next in rotation first, keys that are cooling down last-resort only."""
        with self._lock:
            n = len(keys)
            start = self._next % n
            self._next += 1
            ordered = [keys[(start + i) % n] for i in range(n)]
            now = time.monotonic()
            ready = [k for k in ordered if self._cool.get(_kid(k), 0.0) <= now]
            return ready or ordered      # all resting: still try, a credit top-up may have landed

    def cool(self, key: str, seconds: float) -> None:
        with self._lock:
            self._cool[_kid(key)] = time.monotonic() + seconds

    def allow(self, key: str) -> bool:
        with self._lock:
            guard = self._guards.setdefault(_kid(key), _RateGuard(_max_runs()))
        return guard.allow()


_pool = _KeyPool()
_cache: "OrderedDict[str, tuple[float, str]]" = OrderedDict()
_cache_lock = threading.Lock()
_slots = threading.BoundedSemaphore(2)   # at most two sandboxes at once


def _cache_get(key: str) -> str | None:
    with _cache_lock:
        hit = _cache.get(key)
        if hit and time.monotonic() - hit[0] < CACHE_TTL_S:
            _cache.move_to_end(key)
            return hit[1]
        _cache.pop(key, None)
    return None


def _cache_put(key: str, value: str) -> None:
    with _cache_lock:
        _cache[key] = (time.monotonic(), value)
        while len(_cache) > CACHE_MAX:
            _cache.popitem(last=False)


def _classify(exc: Exception) -> float | None:
    """Seconds to rest the key if `exc` is about the KEY (rate limit, bad key, no credit); None otherwise."""
    status = None
    for obj in (exc, getattr(exc, "response", None)):
        for attr in ("status_code", "status"):
            v = getattr(obj, attr, None)
            if isinstance(v, int):
                status = v
                break
        if status is not None:
            break
    name, msg = type(exc).__name__.lower(), str(exc).lower()
    if status == 429 or "ratelimit" in name or "rate limit" in msg or "too many requests" in msg:
        return COOLDOWN_RATE_LIMIT_S
    if (status in (401, 402, 403)
            or any(w in name for w in ("auth", "permission", "quota", "payment"))
            or any(w in msg for w in ("unauthorized", "invalid api key", "invalid token", "forbidden",
                                      "quota", "insufficient", "credit", "payment required"))):
        return COOLDOWN_BAD_KEY_S
    return None


# ------------------------------------------------------------------ local fallback
# How to call each fixed script's own run() in-process. The signatures differ, so each gets one adapter.
_LOCAL_RUNNERS: dict[str, Callable[[Any, str, dict, dict], dict]] = {
    TABLE_SCRIPT: lambda mod, text, params, extra: mod.run(text, params),
    CALC_SCRIPT: lambda mod, text, params, extra: mod.run(params),
    AFFINITY_SCRIPT: lambda mod, text, params, extra: mod.run(params, json.loads(extra["affinity.json"])),
}


@lru_cache(maxsize=8)
def _local_module(script_name: str):
    """Load a sandbox script as a module without running its main(). Same file the microVM gets."""
    path = SCRIPT_DIR / script_name
    spec = importlib.util.spec_from_file_location(f"lilyai_sandbox_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_local(script_name: str, input_text: str, params: dict[str, Any],
              extra_files: dict[str, str] | None = None) -> str:
    """Blocking. Run a fixed sandbox script in this process. Raises SandboxError with the script's own message on a bad
    parameter, or _LocalTooLarge (a SandboxError) when the input is bigger than the local limit."""
    runner = _LOCAL_RUNNERS.get(script_name)
    if runner is None:
        raise SandboxError("That operation can't run without the sandbox.")
    extra_files = extra_files or {}
    size = len(input_text) + sum(len(v) for v in extra_files.values())
    if size > _local_max_chars():
        raise _LocalTooLarge(f"The input is too large to run locally ({size:,} characters).")
    try:
        result = runner(_local_module(script_name), input_text, params, extra_files)
    except SandboxError:
        raise
    except Exception:
        log.exception("local sandbox script %s crashed", script_name)
        raise SandboxError("The operation failed.")
    if not result.get("ok"):
        raise SandboxError(str(result.get("error") or "The operation failed."))
    return str(result.get("text") or "")


# ------------------------------------------------------------------ the run
def _default_factory(template: str, ttl: int, api_key: str):
    from pandastack import Client   # imported lazily: the bot must start without the SDK
    client = Client(api_key=api_key)
    try:
        return client.sandboxes.create(template=template, ttl_seconds=ttl)
    except TypeError:               # an SDK version without ttl_seconds on this call
        return client.sandboxes.create(template=template)


def _execute(script_name: str, input_text: str, payload: str, sandbox_factory: Callable[..., Any] | None,
             extra_files: dict[str, str] | None = None) -> str:
    """Blocking. Upload a fixed script (+ optional input text, extra data files and a params.json) to a fresh
    sandbox, run it, return its text result. `extra_files` maps a file name to its text, written under /workspace/.

    Tries the configured keys in rotation; a key-level failure (rate limit, rejected key, no credit)
    rests that key and moves to the next one. Script/operation errors are returned as-is, never retried.
    """
    script = (SCRIPT_DIR / script_name).read_text(encoding="utf-8")
    extra_files = extra_files or {}
    extras_hash = hashlib.sha1("\0".join(f"{k}\0{v}" for k, v in sorted(extra_files.items())).encode("utf-8")).hexdigest()
    cache_key = hashlib.sha1((script_name + "\0" + payload + "\0" + input_text + "\0" + extras_hash).encode("utf-8")).hexdigest()
    if (cached := _cache_get(cache_key)) is not None:
        return cached

    keys = load_keys()
    if sandbox_factory is None:
        if not (keys and sdk_installed()):
            raise SandboxError("The sandbox isn't set up (PANDASTACK_API_KEY or the pandastack package is missing).")
        sandbox_factory = _default_factory
    elif not keys:
        keys = ["test-key"]          # injected factories (tests) don't need a real key
    if not _slots.acquire(timeout=10):
        raise SandboxError("The sandbox is busy right now. Try again in a moment.")

    template = os.getenv("PANDASTACK_TEMPLATE", "code-interpreter")
    key_failed = 0
    try:
        for key in _pool.order(keys):
            if not _pool.allow(key):
                continue
            sbx = None
            try:
                sbx = sandbox_factory(template, SANDBOX_TTL_S, key)
                if input_text:
                    sbx.filesystem.write("/workspace/input.md", input_text)
                for fname, content in extra_files.items():
                    sbx.filesystem.write(f"/workspace/{fname}", content)
                sbx.filesystem.write("/workspace/params.json", payload)
                sbx.filesystem.write(f"/workspace/{script_name}", script)
                res = sbx.exec(f"python3 /workspace/{script_name}", timeout_seconds=EXEC_TIMEOUT_S)
                stdout = (getattr(res, "stdout", "") or "").strip()
                code = getattr(res, "exit_code", 0)
                if code not in (0, None) and not stdout:
                    log.warning("sandbox script exited %s: %s", code, (getattr(res, "stderr", "") or "")[:300])
                    raise SandboxError("The sandbox script failed.")
                try:
                    data = json.loads(stdout)
                except json.JSONDecodeError:
                    log.warning("sandbox returned non-JSON output: %r", stdout[:200])
                    raise SandboxError("The sandbox returned an unreadable result.")
                if not data.get("ok"):
                    raise SandboxError(str(data.get("error") or "The operation failed."))
                result = str(data.get("text") or "")
                _cache_put(cache_key, result)
                return result
            except SandboxError:
                raise
            except Exception as e:
                rest = _classify(e)
                if rest is None:
                    log.warning("sandbox call failed: %s: %s", type(e).__name__, str(e)[:200])
                    raise SandboxError("Couldn't reach the sandbox service. Try again in a minute.")
                key_failed += 1
                _pool.cool(key, rest)
                log.warning("pandastack key %s resting %ds (%s); trying the next key", _kid(key), rest, type(e).__name__)
            finally:
                if sbx is not None:
                    try:
                        sbx.kill()
                    except Exception:
                        pass   # TTL reaps it
        if key_failed:
            raise SandboxError("Every PandaStack key is rate limited or out of credit right now. Try again later.")
        raise SandboxError("Sandbox limit reached for this hour. Try again later.")
    finally:
        _slots.release()


def _execute_ex(script_name: str, input_text: str, payload: str, sandbox_factory: Callable[..., Any] | None,
                extra_files: dict[str, str] | None = None, *, fallback: bool = True) -> tuple[str, bool]:
    """Sandbox first, the same script in-process if the sandbox can't be used. Returns (text, ran_in_sandbox).

    A script error (bad parameter) is the same error either way, so it is raised, not hidden. If the input is too big
    for the local path, the sandbox's own error is raised instead.
    """
    try:
        return _execute(script_name, input_text, payload, sandbox_factory, extra_files), True
    except SandboxError as sandbox_error:
        if not (fallback and local_fallback_enabled()):
            raise
        first = sandbox_error
    log.info("%s: sandbox unavailable or refused (%s); running the same script locally", script_name, first)
    try:
        return run_local(script_name, input_text, json.loads(payload), extra_files), False
    except _LocalTooLarge:
        raise first


def run_table_op_ex(text: str, params: dict[str, Any], *,
                    sandbox_factory: Callable[..., Any] | None = None) -> tuple[str, bool]:
    """Table operations (top, stat, filter, compare...) on raw doc text. Returns (text, ran_in_sandbox)."""
    payload = json.dumps(params, sort_keys=True, ensure_ascii=False)
    return _execute_ex(TABLE_SCRIPT, text, payload, sandbox_factory)


def run_calc_ex(calculator: str, inputs: dict[str, Any], *,
                sandbox_factory: Callable[..., Any] | None = None) -> tuple[str, bool]:
    """Rule-based game calculators (PvP score, sparks, race maths...). Returns (text, ran_in_sandbox)."""
    payload = json.dumps({"calculator": calculator, "inputs": inputs}, sort_keys=True, ensure_ascii=False)
    return _execute_ex(CALC_SCRIPT, "", payload, sandbox_factory)


def run_affinity_ex(params: dict[str, Any], data_json: str, *,
                    sandbox_factory: Callable[..., Any] | None = None) -> tuple[str, bool]:
    """Affinity totals and searches. `data_json` is the affinity file (whole, or a slice for one calculation).
    Returns (text, ran_in_sandbox). See sandbox_scripts/affinity_calc.py."""
    payload = json.dumps(params, sort_keys=True, ensure_ascii=False)
    return _execute_ex(AFFINITY_SCRIPT, "", payload, sandbox_factory, extra_files={"affinity.json": data_json})


def run_table_op(text: str, params: dict[str, Any], *, sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Table operations (top, stat, filter, compare...) on raw doc text. See sandbox_scripts/docs_table_ops.py."""
    return run_table_op_ex(text, params, sandbox_factory=sandbox_factory)[0]


def run_calc(calculator: str, inputs: dict[str, Any], *, sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Rule-based game calculators (PvP score, sparks, race maths...). See sandbox_scripts/game_calcs.py."""
    return run_calc_ex(calculator, inputs, sandbox_factory=sandbox_factory)[0]


def run_affinity(params: dict[str, Any], data_json: str, *, sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Affinity totals and searches. See sandbox_scripts/affinity_calc.py."""
    return run_affinity_ex(params, data_json, sandbox_factory=sandbox_factory)[0]


async def run_table_op_async(text: str, params: dict[str, Any], **kw: Any) -> str:
    return await asyncio.to_thread(run_table_op, text, params, **kw)


async def run_calc_async(calculator: str, inputs: dict[str, Any], **kw: Any) -> str:
    return await asyncio.to_thread(run_calc, calculator, inputs, **kw)


async def run_affinity_async(params: dict[str, Any], data_json: str, **kw: Any) -> str:
    return await asyncio.to_thread(run_affinity, params, data_json, **kw)


async def run_table_op_ex_async(text: str, params: dict[str, Any], **kw: Any) -> tuple[str, bool]:
    return await asyncio.to_thread(run_table_op_ex, text, params, **kw)


async def run_calc_ex_async(calculator: str, inputs: dict[str, Any], **kw: Any) -> tuple[str, bool]:
    return await asyncio.to_thread(run_calc_ex, calculator, inputs, **kw)


async def run_affinity_ex_async(params: dict[str, Any], data_json: str, **kw: Any) -> tuple[str, bool]:
    return await asyncio.to_thread(run_affinity_ex, params, data_json, **kw)
