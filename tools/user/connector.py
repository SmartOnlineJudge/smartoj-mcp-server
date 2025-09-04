from backend.connector import BaseBackendConnector


class UserBackendConnector(BaseBackendConnector):
    async def get_current_user(self):
        response = await self.client.get("/user")
        return self.parse_response(response)
