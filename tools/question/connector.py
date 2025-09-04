from backend.connector import BaseBackendConnector


class QuestionBackendConnector(BaseBackendConnector):
    async def query_all_languages(self):
        response = await self.client.get("/question/languages")
        return self.parse_response(response)
