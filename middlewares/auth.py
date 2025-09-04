from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.server.dependencies import get_http_headers

from exceptions.auth import AuthenticationError

import settings


BACKEND_SESSION_ID_NAME = settings.BACKEND_SESSION_ID_NAME


class RequireBackendSessionIDMiddleware(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        headers = get_http_headers()
        backend_session_id = headers.get(BACKEND_SESSION_ID_NAME)
        
        if not backend_session_id:
            raise AuthenticationError()

        context.fastmcp_context.set_state(BACKEND_SESSION_ID_NAME, backend_session_id)

        return await call_next(context)
