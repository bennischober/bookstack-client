"""Base resource class for BookStack API client."""

# from ..client import BookStackClient
# create BookStackClient.pyi to avoid circular import issues?
from ..utils import HttpMethod


class BaseResource:
    """Base resource class for BookStack API client."""

    def __init__(self, client):
        self._client = client

    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        return self._client._request(method, endpoint, **kwargs)

    def _get_paginated(self, endpoint: str, **kwargs) -> list:
        return self._client._get_paginated_content(HttpMethod.GET.value, endpoint, **kwargs)
