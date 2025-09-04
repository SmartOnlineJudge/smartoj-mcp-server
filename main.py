import asyncio

from fastmcp import FastMCP

from middlewares.auth import RequireBackendSessionIDMiddleware
from tools.user.tool import user_mcp
from tools.question.tool import question_mcp
from tools.management.tool import management_mcp


async def setup():
    smartoj_mcp = FastMCP("智能算法刷题平台——MCP服务器")
    smartoj_mcp.add_middleware(RequireBackendSessionIDMiddleware())

    await smartoj_mcp.import_server(user_mcp)
    await smartoj_mcp.import_server(question_mcp)
    await smartoj_mcp.import_server(management_mcp)

    await smartoj_mcp.run_async("http")


if __name__ == "__main__":
    try:
        asyncio.run(setup())
    except KeyboardInterrupt:
        pass
 