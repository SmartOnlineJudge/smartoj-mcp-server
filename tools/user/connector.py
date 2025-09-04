from fastmcp.server.context import Context

from backend.connector import BaseBackendConnector


class UserBackendConnector(BaseBackendConnector):
    async def get_current_user(self, context: Context):
        response = await self.client.get("/user", context)
        return self.parse_response(response)
