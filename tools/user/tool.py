from fastmcp import FastMCP, Context

from .connector import UserBackendConnector


user_mcp = FastMCP("User MCP")
user_connector = UserBackendConnector()


@user_mcp.tool(description="获取当前用户的信息")
async def get_current_user(context: Context):
    return await user_connector.get_current_user(context)
