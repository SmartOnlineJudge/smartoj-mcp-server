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

    async def detect_permission(self, question_id: int):
        json_data = {"question_id": question_id}
        return await self.client.post("/question/permission-detection", json=json_data)

    async def create_test_for_question(self, question_id: int, input_output: str):
        json_data = {
            "question_id": question_id,
            "input_output": input_output,
        }
        return await self.client.post("/question/test", json=json_data)

    async def create_memory_time_limit_for_question(
        self, 
        question_id: int, 
        language_id: int, 
        memory_limit: int, 
        time_limit: int
    ):
        json_data = {
            "question_id": question_id,
            "language_id": language_id,
            "memory_limit": memory_limit,
            "time_limit": time_limit,
        }
        return await self.client.post("/question/memory-time-limit", json=json_data)

    async def create_judge_template_for_question(
        self, 
        question_id: int, 
        language_id: int, 
        code: str
    ):
        json_data = {
            "question_id": question_id,
            "language_id": language_id,
            "code": code,
        }
        return await self.client.post("/question/judge-template", json=json_data)

    async def create_solving_framework_for_question(
        self, 
        question_id: int, 
        language_id: int, 
        code_framework: str
    ):
        json_data = {
            "question_id": question_id,
            "language_id": language_id,
            "code_framework": code_framework,
        }
        return await self.client.post("/question/solving-framework", json=json_data)
