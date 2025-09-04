from fastmcp import FastMCP, Context

from .connector import QuestionBackendConnector


question_mcp = FastMCP("Question MCP")
question_connector = QuestionBackendConnector()
