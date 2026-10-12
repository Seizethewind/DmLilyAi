import asyncio

from LilyAiTool.Executor.executor import ToolExecutor
from LilyAiTool.Models.tool_models import ToolContextData, ToolSpec
from LilyAiTool.Registry.registry import ToolRegistry


def test_executor_rejects_a_category_outside_the_request_context():
    registry = ToolRegistry()
    called = []

    def handler(ctx, args):
        called.append(True)
        return "should not run"

    registry.register(ToolSpec("restricted", "restricted", {"type": "object"}, handler, category="admin"))
    result = asyncio.run(ToolExecutor(registry).execute("restricted", {}, ToolContextData(allowed_categories=frozenset({"utility"}))))
    assert not result.ok
    assert "not authorized" in result.output
    assert called == []


def test_internal_context_can_run_a_registered_tool():
    registry = ToolRegistry()
    registry.register(ToolSpec("utility", "utility", {"type": "object"}, lambda ctx, args: "ok"))
    result = asyncio.run(ToolExecutor(registry).execute("utility", {}, ToolContextData()))
    assert result.ok
    assert result.output == "ok"
