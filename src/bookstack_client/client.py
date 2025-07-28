"""BookStack API client."""

import httpx
from typing import Any
from .exceptions import create_api_error, create_connection_error
from .resources import AuditLogResource


class BookStackClient:
    """Client for interacting with BookStack API."""

    def __init__(
        self,
        base_url: str,
        token_id: str,
        token_secret: str,
        verify_ssl: bool = True,
        timeout: float = 30.0,
        **client_kwargs: Any,
    ) -> None:
        """
        Initialize BookStack client.

        Args:
            base_url (str): Base URL of BookStack instance
            token_id (str): API token ID
            token_secret (str): API token secret
            verify_ssl (bool): Whether to verify SSL certificates
            timeout (float): Request timeout in seconds
            **client_kwargs (Any): Additional arguments passed to `httpx.Client`
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        # Default headers
        headers = {
            "Authorization": f"Token {token_id}:{token_secret}",
            "Content-Type": "application/json",
            "User-Agent": "bookstack-client/0.1.0",
        }

        # Merge with any custom headers
        if "headers" in client_kwargs:
            headers.update(client_kwargs.pop("headers"))

        self._client = httpx.Client(
            base_url=f"{self.base_url}/api",
            headers=headers,
            timeout=timeout,
            verify=verify_ssl,
            **client_kwargs,
        )

        self.audit_log = AuditLogResource(self)

    def __enter__(self) -> "BookStackClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            self._client.close()

    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any
    ) -> dict[str, Any]:
        """Make HTTP request to BookStack API.

        Args:
            method: HTTP method
            endpoint: API endpoint (without /api prefix)
            **kwargs: Additional arguments passed to httpx request

        Returns:
            JSON response as dictionary

        Raises:
            BookStackAPIError: For HTTP errors with API error details
            BookStackError: For connection/request errors
        """
        try:
            response = self._client.request(method, endpoint, **kwargs)
            response.raise_for_status()

            # Handle empty responses (like DELETE operations)
            if response.status_code == 204 or not response.text:
                return {}

            return response.json()

        except httpx.HTTPStatusError as e:
            raise create_api_error(e.response) from e

        except httpx.RequestError as e:
            raise create_connection_error(e) from e

    def _get_paginated_content(
            self,
            method: str,
            url: str,
            count: int = 100,
            max_items: int | None = None,
            **kwargs: Any
    ) -> list:
        """
        Helper method to fetch paginated content with configurable parameters. For more information about pagination, check the BookStack API docs: https://demo.bookstackapp.com/api/docs#listing-endpoints

        Args:
            method (str): The HTTP method to use for the request.
            url (str): The URL to fetch the paginated content from.
            count (int): Number of items per page (default: 100).
            max_items (int | None): Maximum number of items to fetch (None for all).
            **kwargs (Any): Additional keyword arguments to pass to the request.

        Returns:
            list: A list of items fetched from the paginated endpoint.
        """
        items = []
        offset = 0

        while True:
            # Build URL with offset and count parameters
            separator = '&' if '?' in url else '?'
            paginated_url = f"{url}{separator}offset={offset}&count={count}"

            response = self._client.request(method, paginated_url, **kwargs)
            response.raise_for_status()
            data: dict = response.json()

            page_items = data.get('data', [])
            items.extend(page_items)

            total = data.get('total', 0)

            # Break conditions
            if (len(items) >= total or
                len(page_items) == 0 or
                    (max_items and len(items) >= max_items)):
                break

            # Move to next page
            offset += count

        # Trim to max_items if specified
        if max_items and len(items) > max_items:
            items = items[:max_items]

        return items
