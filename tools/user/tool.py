from fastmcp import FastMCP

from .connector import UserBackendConnector


user_mcp = FastMCP("User MCP")
user_connector = UserBackendConnector()


@user_mcp.tool
async def get_current_user() -> str:
    """
    获取当前用户的信息。

    在调用这个工具的时候你不需要输入任何参数。

    你可以通过这个工具来获取当前用户的详细信息。
    """
    response = await user_connector.get_current_user()
    if not response:
        return "获取用户信息失败"
    result = ""
    for k, v in response["data"].items():
        result += f"{k}: {v}\n"
    return result
