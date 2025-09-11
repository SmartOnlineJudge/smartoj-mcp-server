from fastmcp import FastMCP

from .connector import QuestionBackendConnector


question_mcp = FastMCP("Question MCP")
question_connector = QuestionBackendConnector()


@question_mcp.tool
async def query_all_programming_languages() -> str:
    """
    查询所有编程语言信息。

    在调用这个工具的时候你不需要输入任何参数。

    你可以通过这个工具查询到数据库中所有的编程语言的详细信息。

    一个编程语言通常包括以下字段：
    - id: 该编程语言在数据库中的唯一标识
    - name: 编程语言的名称
    - version: 编程语言的版本
    - is_deleted: 该编程语言是否已经不使用了
    """
    response = await question_connector.query_all_languages()
    if not response:
        return "获取编程语言失败"
    result = ""
    for language in response["data"]:
        for key, value in language.items():
            result += f"{key}: {value} "
        result += "\n"
    return result


@question_mcp.tool
async def query_all_tags():
    """
    查询所有标签信息。

    在调用这个工具的时候你不需要输入任何参数。

    你可以通过这个工具查询到数据库中所有的标签的详细信息。

    一个标签通常包括以下字段：
    - id: 该标签在数据库中的唯一标识
    - name: 标签的名称
    - score: 标签的分数。分数越高，代表该标签对应的题目的难度系数越高
    """
    response = await question_connector.query_all_tags()
    if not response:
        return "获取标签失败"
    results = []
    for tag in response["data"]:
        if tag["is_deleted"]:
            continue
        tag.pop("is_deleted")
        tag.pop("created_at")
        results.append(tag)
    return results


@question_mcp.tool
async def query_judge_templates_of_question(question_id: int):
    """
    查询一个题目的所有判题模板信息。

    在调用这个工具时你需要输入一个参数：
    - question_id: 题目的id

    你可以通过这个工具查询到数据库中指定题目的所有评测模板的详细信息。

    一个判题模板通常包括以下字段：
    - id: 该评测模板在数据库中的唯一标识
    - code: 判题模板的代码
    - language: 评测模板对应的编程语言（对象类型）
      - id: 该编程语言在数据库中的唯一标识
      - name: 编程语言的名称
    """
    response = await question_connector.query_question_related_data(question_id, "judge-templates")
    try:
        data = response["data"]
    except KeyError:
        return "获取判题模板失败"
    if not data:
        return "该题目暂时没有判题模板"
    return data


@question_mcp.tool
async def query_memory_time_limits_of_question(question_id: int):
    """
    查询一个题目的内存时间限制。

    在调用这个工具时你需要输入一个参数：
    - question_id: 题目的id

    你可以通过这个工具查询到数据库中指定题目的内存时间限制。

    一个内存时间限制通常包括以下字段：
    - id: 该内存时间限制在数据库中的唯一标识
    - memory_limit: 题目的内存限制(单位 MB)
    - time_limit: 题目的时间限制(单位 ms)
    - language: 评测模板对应的编程语言（对象类型）
      - id: 该编程语言在数据库中的唯一标识
      - name: 编程语言的名称
    """
    response = await question_connector.query_question_related_data(question_id, "memory-time-limits")
    try:
        data = response["data"]
    except KeyError:
        return "获取内存时间限制失败"
    if not data:
        return "该题目暂时没有内存时间限制"
    return data


@question_mcp.tool
async def query_solving_frameworks_of_question(question_id: int):
    """
    查询一个题目的解题框架信息。

    在调用这个工具时你需要输入一个参数：
    - question_id: 题目的id

    你可以通过这个工具查询到数据库中指定题目的所有解题框架的详细信息。

    一个解题框架通常包括以下字段：
    - id: 该解题框架在数据库中的唯一标识
    - code_framework: 解题框架的代码
    - language: 评测模板对应的编程语言（对象类型）
      - id: 该编程语言在数据库中的唯一标识
      - name: 编程语言的名称
    """
    response = await question_connector.query_question_related_data(question_id, "solving-frameworks")
    try:
        data = response["data"]
    except KeyError:
        return "获取解题框架失败"
    if not data:
        return "该题目暂时没有解题框架"
    return data


@question_mcp.tool
async def query_tests_of_question(question_id: int):
    """
    查询一个题目的所有测试用例信息。

    在调用这个工具时你需要输入一个参数：
    - question_id: 题目的id

    你可以通过这个工具查询到数据库中指定题目的所有测试用例的详细信息。

    一个测试用例通常包括以下字段：
    - id: 该测试用例在数据库中的唯一标识
    - input_output: 测试用例的原始输入输出信息
    """
    response = await question_connector.query_question_related_data(question_id, "tests")
    try:
        data = response["data"]
    except KeyError:
        return "获取测试用例失败"
    if not data:
        return "该题目暂时没有测试用例"
    return data


@question_mcp.tool
async def query_question_info(question_id: int):
    """
    查询一个题目的详细信息。

    在调用这个工具时你需要输入一个参数：
    - question_id: 题目的id

    你可以通过这个工具查询到数据库中指定题目的部分详细信息。

    你可以获取到该题目的部分字段对应的信息：
    - id: 该题目在数据库中的唯一标识
    - title: 题目的标题
    - description: 题目的描述
    - difficulty: 题目的难度
    - tags: 题目的标签
        - name: 标签的名称
    """
    response = await question_connector.query_question_info(question_id)
    if not response:
        return "该题目不存在"
    try:
        data: dict = response["data"]
    except KeyError:
        return "获取题目信息失败"
    result = {
        "id": data["id"],
        "title": data["title"],
        "description": data["description"],
        "difficulty": data["difficulty"],
        "tags": [tag["tag"]["name"] for tag in data["tags"]],
    }
    return result
