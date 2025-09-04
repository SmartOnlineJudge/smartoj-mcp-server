from json import JSONDecodeError

from httpx import Response

import settings
from .http_client import AsyncClient


class BaseBackendConnector:
    def __init__(self):
        self.client = AsyncClient(base_url=settings.BACKEDN_URL)

    def parse_response(self, response: Response):
        try:
            return response.json()
        except JSONDecodeError:
            return {}
