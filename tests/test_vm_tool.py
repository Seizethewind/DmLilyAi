"""Tests for the Chat Mode VM tool (run_code). No network: the microVM is faked.

Run:  python -m pytest tests/test_vm_tool.py -v
"""
import asyncio
import importlib

import pytest


class _FS:
    def __init__(self, files):
        self.files = files

    def write(self, path, content):
        self.files[path] = content


class _Res:
    def __init__(self, stdout="", stderr="", exit_code=0):
        self.stdout, self.stderr, self.exit_code = stdout, stderr, exit_code


class _FakeSandbox:
    def __init__(self, result=None, exc=None):
        self.files = {}
        self.filesystem = _FS(self.files)
        self.result = result if result is not None else _Res("hello\n")
        self.exc = exc
        self.cmds = []
        self.killed = False

    def exec(self, cmd, timeout_seconds=30):
        self.cmds.append((cmd, timeout_seconds))
        if self.exc:
            raise self.exc
        return self.result

    def kill(self):
        self.killed = True


class _RateLimited(Exception):
    status_code = 429


@pytest.fixture()
def vm(monkeypatch):
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner, vm_runner

    monkeypatch.setenv("PANDASTACK_API_KEY", "")
    monkeypatch.delenv("LILYAI_VM_MAX_RUNS_PER_HOUR", raising=False)
    monkeypatch.delenv("LILYAI_SANDBOX_LOCAL_FALLBACK", raising=False)
    sandbox_runner._pool = sandbox_runner._KeyPool()
    vm_runner._guard = None
    return vm_runner


# ---- the runner ----
def test_runs_python_in_the_vm_and_reports_the_output(vm):
    sbx = _FakeSandbox()
    out = vm.run_code("python", "print('hello')", sandbox_factory=lambda template, ttl, key: sbx)
    assert "exit code: 0" in out and "hello" in out
    assert sbx.files["/workspace/main.py"] == "print('hello')"
    assert sbx.cmds == [("python3 /workspace/main.py", 30)]
    assert sbx.killed is True


def test_runs_bash_and_defaults_to_python(vm):
    sbx = _FakeSandbox()
    vm.run_code("bash", "echo hi", sandbox_factory=lambda template, ttl, key: sbx)
    assert sbx.files["/workspace/main.sh"] == "echo hi" and sbx.cmds[0][0] == "bash /workspace/main.sh"
    other = _FakeSandbox()
    vm.run_code(None, "print(1)", sandbox_factory=lambda template, ttl, key: other)
    assert other.cmds[0][0] == "python3 /workspace/main.py"


def test_timeout_is_clamped(vm):
    sbx = _FakeSandbox()
    vm.run_code("python", "print(1)", timeout_s=9999, sandbox_factory=lambda template, ttl, key: sbx)
    assert sbx.cmds[0][1] == vm.MAX_TIMEOUT_S


def test_a_failing_script_returns_its_error_instead_of_raising(vm):
    sbx = _FakeSandbox(_Res("", "Traceback (most recent call last):\nValueError: boom", 1))
    out = vm.run_code("python", "raise ValueError('boom')", sandbox_factory=lambda template, ttl, key: sbx)
    assert "exit code: 1" in out and "ValueError: boom" in out and "stdout: (empty)" in out


def test_no_key_never_runs_locally(vm, monkeypatch):
    from LilyAiGameSpace import sandbox_runner

    def boom(*a, **k):
        raise AssertionError("model-written code must never run in the bot")

    monkeypatch.setattr(sandbox_runner, "run_local", boom)
    assert sandbox_runner.local_fallback_enabled() is True      # the fallback is on, and still isn't used
    with pytest.raises(vm.SandboxError, match="isn't set up"):
        vm.run_code("python", "print(1)")
    assert vm.is_available() is False


def test_every_key_rate_limited_is_an_error_not_a_local_run(vm, monkeypatch):
    monkeypatch.setenv("PANDASTACK_API_KEY", "k1,k2")

    def factory(template, ttl, key):
        raise _RateLimited("too many requests")

    with pytest.raises(vm.SandboxError, match="rate limited"):
        vm.run_code("python", "print(1)", sandbox_factory=factory)


def test_the_next_key_is_tried_when_the_first_is_rate_limited(vm, monkeypatch):
    monkeypatch.setenv("PANDASTACK_API_KEY", "k1,k2")
    tried = []

    def factory(template, ttl, key):
        tried.append(key)
        if key == "k1":
            raise _RateLimited("too many requests")
        return _FakeSandbox()

    assert "hello" in vm.run_code("python", "print(1)", sandbox_factory=factory)
    assert tried == ["k1", "k2"]


def test_bad_input_is_refused_before_a_vm_boots(vm):
    booted = []

    def factory(template, ttl, key):
        booted.append(key)
        return _FakeSandbox()

    for language, code in [("ruby", "puts 1"), ("python", ""), ("python", "   "), ("python", "x" * (vm.MAX_CODE_CHARS + 1))]:
        with pytest.raises(vm.SandboxError):
            vm.run_code(language, code, sandbox_factory=factory)
    assert booted == []


def test_hourly_cap_on_code_runs(vm, monkeypatch):
    monkeypatch.setenv("LILYAI_VM_MAX_RUNS_PER_HOUR", "2")
    factory = lambda template, ttl, key: _FakeSandbox()      # noqa: E731
    vm.run_code("python", "print(1)", sandbox_factory=factory)
    vm.run_code("python", "print(2)", sandbox_factory=factory)
    with pytest.raises(vm.SandboxError, match="limit reached"):
        vm.run_code("python", "print(3)", sandbox_factory=factory)


def test_long_output_keeps_the_start_and_the_end(vm):
    sbx = _FakeSandbox(_Res("A" * 5000 + "Z" * 5000))
    out = vm.run_code("python", "print(1)", sandbox_factory=lambda template, ttl, key: sbx)
    assert "characters cut" in out and "AAAA" in out and out.rstrip().endswith("ZZZZ")
    assert len(out) < 4000


def test_running_past_the_limit_is_reported(vm):
    sbx = _FakeSandbox(exc=TimeoutError("exec timed out"))
    with pytest.raises(vm.SandboxError, match="ran past"):
        vm.run_code("python", "while True: pass", sandbox_factory=lambda template, ttl, key: sbx)
    assert sbx.killed is True


def test_an_unreachable_service_is_a_plain_error(vm):
    def factory(template, ttl, key):
        raise RuntimeError("connection refused")

    with pytest.raises(vm.SandboxError, match="Couldn't reach"):
        vm.run_code("python", "print(1)", sandbox_factory=factory)


# ---- the tool the chat model sees ----
@pytest.fixture()
def tool(vm, monkeypatch):
    from LilyAiGameSpace import sandbox_runner

    monkeypatch.setenv("PANDASTACK_API_KEY", "psk_test")
    monkeypatch.setattr(sandbox_runner, "sdk_installed", lambda: True)
    monkeypatch.setenv("LILYAI_VM_USER_IDS", "42")
    monkeypatch.delenv("ALLOWED_USER_IDS", raising=False)
    monkeypatch.delenv("LILYAI_VM_TOOL", raising=False)
    return importlib.import_module("LilyAiTool.VmTools.vm_tools")


def test_offered_when_configured_switched_on_and_someone_is_allowed(tool):
    specs = tool.vm_tools()
    assert [s.name for s in specs] == ["run_code"] and specs[0].category == "vm"
    assert specs[0].parameters["required"] == ["code"]


def test_hidden_without_a_real_sandbox_even_though_the_local_fallback_is_on(tool, monkeypatch):
    monkeypatch.setenv("PANDASTACK_API_KEY", "")
    assert tool.vm_tools() == []


def test_hidden_when_switched_off(tool, monkeypatch):
    for value in ("0", "false", "off", "no"):
        monkeypatch.setenv("LILYAI_VM_TOOL", value)
        assert tool.vm_tools() == [], value


def test_hidden_when_nobody_is_allowed(tool, monkeypatch):
    monkeypatch.delenv("LILYAI_VM_USER_IDS", raising=False)
    assert tool.vm_tools() == []


def test_falls_back_to_allowed_user_ids(tool, monkeypatch):
    monkeypatch.delenv("LILYAI_VM_USER_IDS", raising=False)
    monkeypatch.setenv("ALLOWED_USER_IDS", "7, 8")
    assert tool.allowed_user_ids() == frozenset({"7", "8"}) and len(tool.vm_tools()) == 1


def test_handler_runs_code_for_an_allowed_user(tool, vm, monkeypatch):
    from LilyAiTool.Models.tool_models import ToolContextData

    seen = {}

    def fake(language, code, **kw):
        seen.update(language=language, code=code, **kw)
        return "exit code: 0\nstdout:\n4"

    monkeypatch.setattr(vm, "run_code", fake)
    out = asyncio.run(tool._run_code(ToolContextData("42", "Me"), {"code": "print(2+2)", "language": None}))
    assert "stdout:\n4" in out and seen["language"] == "python" and seen["code"] == "print(2+2)"


def test_handler_refuses_a_user_who_is_not_on_the_list(tool, vm, monkeypatch):
    from LilyAiCore.Exceptions.errors import ToolError
    from LilyAiTool.Models.tool_models import ToolContextData

    monkeypatch.setattr(vm, "run_code", lambda *a, **k: pytest.fail("must not run"))
    with pytest.raises(ToolError, match="isn't enabled"):
        asyncio.run(tool._run_code(ToolContextData("7", "Other"), {"code": "print(1)"}))


def test_a_vm_failure_becomes_a_tool_error(tool, vm, monkeypatch):
    from LilyAiCore.Exceptions.errors import ToolError
    from LilyAiTool.Models.tool_models import ToolContextData

    def fake(language, code, **kw):
        raise vm.SandboxError("VM run limit reached for this hour. Try again later.")

    monkeypatch.setattr(vm, "run_code", fake)
    with pytest.raises(ToolError, match="limit reached"):
        asyncio.run(tool._run_code(ToolContextData("42", "Me"), {"code": "print(1)"}))


def test_only_chat_mode_gets_the_vm_category():
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiMain.MainService.Interaction.Modes import MODES

    assert "vm" in MODES["chat"].categories
    assert not [k for k, m in MODES.items() if k != "chat" and "vm" in m.categories]
