"""Groq tool: run code the model writes in a throwaway Linux VM. Optional, and only in Chat Mode.

The code runs in a PandaStack microVM (LilyAiGameSpace/vm_runner.py), never inside the bot, and never through the
sandbox_runner local fallback. The tool is only offered when ALL of these hold:

    - a PandaStack key is set and the pandastack package is installed,
    - LILYAI_VM_TOOL is not switched off (default on),
    - at least one Discord user id is allowed: LILYAI_VM_USER_IDS, or if that is empty, ALLOWED_USER_IDS.

The handler checks the user id again on every call, so a model can't run code for someone who isn't on the list.
"""
from __future__ import annotations

import os

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiGameSpace import vm_runner
from LilyAiGameSpace.sandbox_runner import SandboxError
from LilyAiTool.Models.tool_models import ToolSpec

CATEGORY = "vm"

DESCRIPTION = (
    "Run code in a throwaway Linux VM (Python 3 or bash) and get its output back. Use it only when the task really needs "
    "running code: processing or parsing data the user pasted, testing a snippet, a calculation too long for 'calculate'. "
    "Do NOT use it for anything web_search, 'calculate' or 'current_time' can answer. Print every result you need: only "
    "stdout, stderr and the exit code come back. Each call is a fresh VM, so nothing is kept between calls and variables "
    "don't carry over. The time limit is 30 seconds by default (60 at most). Internet access from inside the VM is not "
    "guaranteed. Quote the output exactly as returned. If the exit code isn't 0, read stderr and fix the code; never "
    "guess what the output would have been."
)


def _id_set(name: str) -> frozenset[str]:
    return frozenset(x.strip() for x in os.getenv(name, "").split(",") if x.strip().isdigit())


def allowed_user_ids() -> frozenset[str]:
    """LILYAI_VM_USER_IDS if set, else ALLOWED_USER_IDS. Empty means nobody, and then the tool isn't offered."""
    return _id_set("LILYAI_VM_USER_IDS") or _id_set("ALLOWED_USER_IDS")


def switch_on() -> bool:
    return os.getenv("LILYAI_VM_TOOL", "1").strip().lower() not in ("0", "false", "no", "off")


def enabled() -> bool:
    return switch_on() and vm_runner.is_available() and bool(allowed_user_ids())


async def _run_code(ctx, args: dict) -> str:
    if str(ctx.user_id) not in allowed_user_ids():
        raise ToolError("The VM isn't enabled for this account.")
    language = args.get("language") or "python"
    try:
        out = await vm_runner.run_code_async(language, args["code"], timeout_s=args.get("timeout_seconds"))
    except SandboxError as e:
        raise ToolError(str(e))
    return f"Ran {language} in a fresh VM (nothing is kept between runs):\n{out}"


def vm_tools() -> list[ToolSpec]:
    if not enabled():
        return []
    return [
        ToolSpec(
            "run_code",
            DESCRIPTION,
            {"type": "object", "properties": {
                "code": {"type": "string", "description": "The whole program. Print what you need to see."},
                "language": {"type": ["string", "null"], "description": "python (default) or bash"},
                "timeout_seconds": {"type": ["integer", "null"], "description": "Time limit in seconds: default 30, at most 60"},
            }, "required": ["code"]},
            _run_code,
            category=CATEGORY,
            timeout=90.0,
        ),
    ]
