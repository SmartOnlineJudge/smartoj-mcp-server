from json import JSONDecodeError

from fastmcp.server.context import Context

import settings
from .http_client import AsyncClient


class BackendConnector:
    def __init__(self):
        self.client = AsyncClient(base_url=settings.BACKEDN_URL)

    async def get_cuttent_user(self, context: Context):
        response = await self.client.get("/user", context)
        try:
            return response.json()
        except JSONDecodeError:
            return {}


backend_connector = BackendConnector()
