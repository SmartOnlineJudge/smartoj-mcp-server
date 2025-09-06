import settings
from .http_client import AsyncClient


class BaseBackendConnector:
    def __init__(self):
        self.client = AsyncClient(base_url=settings.BACKEDN_URL)
