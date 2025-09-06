from backend.connector import BaseBackendConnector


class QuestionBackendConnector(BaseBackendConnector):
    async def query_all_languages(self):
        return await self.client.get("/question/languages")
