from enum import Enum


class HttpMethod(str, Enum):
    """Enumeration of HTTP methods used in API requests."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
