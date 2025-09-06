from backend.connector import BaseBackendConnector


class UserBackendConnector(BaseBackendConnector):
    async def get_current_user(self):
        return await self.client.get("/user")
