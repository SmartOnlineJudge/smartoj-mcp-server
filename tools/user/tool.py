from fastmcp import FastMCP

from .connector import UserBackendConnector


user_mcp = FastMCP("User MCP")
user_connector = UserBackendConnector()


@user_mcp.tool(description="获取当前用户的信息")
async def get_current_user():
    return await user_connector.get_current_user()
