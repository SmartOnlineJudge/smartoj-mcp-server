from fastmcp.server.context import Context

import settings


def get_backend_session_id(context: Context) -> str:
    return context.get_state(settings.BACKEND_SESSION_ID_NAME)
