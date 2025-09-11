from backend.connector import BaseBackendConnector


class QuestionBackendConnector(BaseBackendConnector):
    async def query_all_languages(self):
        return await self.client.get("/question/languages")

    async def query_all_tags(self):
        return await self.client.get("/question/tags")

    async def query_question_info(self, question_id: int):
        params = {"question_id": question_id}
        return await self.client.get("/question/online-solving", params=params)

    async def query_question_related_data(self, question_id: int, related_type: str):
        """
        查询一个题目的所有关联数据。

        Args:
            question_id (int): 题目的id
            related_type (str): 关联数据的类型（judge-templates | memory-time-limits | memory-time-limits | tests | sovling-frameworks）
        """
        params = {"question_id": question_id}
        return await self.client.get(f"/question/{related_type}", params=params)
