import asyncio

from fastmcp import FastMCP
from fastmcp.server.context import Context

from middlewares.auth import RequireBackendSessionIDMiddleware
from backend.connector import backend_connector


mcp = FastMCP("智能算法刷题平台——MCP服务器")
mcp.add_middleware(RequireBackendSessionIDMiddleware())


@mcp.tool(description="获取当前登录用户的信息")
async def get_current_user(context: Context):
    return await backend_connector.get_cuttent_user(context)


if __name__ == "__main__":
    try:
        asyncio.run(mcp.run_async("http"))
    except KeyboardInterrupt:
        pass
 