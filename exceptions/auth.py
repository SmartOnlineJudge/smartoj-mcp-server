from fastmcp.exceptions import FastMCPError


class AuthenticationError(FastMCPError):
    def __str__(self):
        return "Access denied: The value of 'backend-session-id' is missing. Please check the request header."
    