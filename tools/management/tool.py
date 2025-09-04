from fastmcp import FastMCP, Context

from .connector import ManagementBackendConnector


management_mcp = FastMCP("Management MCP")
management_connector = ManagementBackendConnector()
