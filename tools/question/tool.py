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
