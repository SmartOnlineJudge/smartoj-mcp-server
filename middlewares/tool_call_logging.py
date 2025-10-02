from uvicorn.config import logger
from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.server.dependencies import get_http_headers

import settings


class ToolCallLoggingMiddleware(Middleware):
    async def on_call_tool(self, context: MiddlewareContext, call_next):
        headers = get_http_headers()
        backend_session_id = headers.get(settings.BACKEND_SESSION_ID_NAME)

        logger.warning(f"Tool Calling: <{context.message.name}> - <{backend_session_id}> - <{context.message.arguments}>")

        result = await call_next(context)
        return result
    