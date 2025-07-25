"""BookStack client exceptions."""

from typing import Any
import httpx


class BookStackError(Exception):
    """Base exception for all BookStack client errors.

    This is the base class that all other BookStack exceptions inherit from.
    Catch this to handle any BookStack-related error.
    """

    def __init__(self, message: str, original_error: Exception | None = None) -> None:
        """Initialize BookStack error.

        Args:
            message: Human-readable error message
            original_error: The original exception that caused this error
        """
        super().__init__(message)
        self.message = message
        self.original_error = original_error

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.message}')"


class BookStackConnectionError(BookStackError):
    """Raised when there are network/connection issues.

    This includes DNS resolution failures, connection timeouts,
    SSL certificate errors, etc.
    """
    pass


class BookStackTimeoutError(BookStackConnectionError):
    """Raised when a request times out."""

    def __init__(self, message: str = "Request timed out", timeout: float | None = None) -> None:
        super().__init__(message)
        self.timeout = timeout


class BookStackAPIError(BookStackError):
    """Raised when the BookStack API returns an HTTP error status.

    This exception provides detailed information about API errors,
    including status codes, error messages, and request details.
    """

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_data: dict[str, Any] | None = None,
        request_url: str | None = None,
        request_method: str | None = None,
    ) -> None:
        """Initialize API error.

        Args:
            message: Human-readable error message
            status_code: HTTP status code from the response
            response_data: Parsed JSON response data (if available)
            request_url: The URL that was requested
            request_method: HTTP method used for the request
        """
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data or {}
        self.request_url = request_url
        self.request_method = request_method

    @property
    def error_code(self) -> str | None:
        """Get the BookStack-specific error code from response."""
        if isinstance(self.response_data, dict):
            return self.response_data.get("error", {}).get("code")
        return None

    @property
    def error_details(self) -> dict[str, Any] | None:
        """Get detailed error information from response."""
        if isinstance(self.response_data, dict):
            return self.response_data.get("error", {}).get("details")
        return None

    def __str__(self) -> str:
        parts = [self.message]
        if self.status_code:
            parts.append(f"Status: {self.status_code}")
        if self.request_method and self.request_url:
            parts.append(f"Request: {self.request_method} {self.request_url}")
        return " | ".join(parts)


class BookStackAuthenticationError(BookStackAPIError):
    """Raised when authentication fails (401 Unauthorized)."""

    def __init__(self, message: str = "Authentication failed") -> None:
        super().__init__(message, status_code=401)


class BookStackPermissionError(BookStackAPIError):
    """Raised when access is forbidden (403 Forbidden)."""

    def __init__(self, message: str = "Access forbidden") -> None:
        super().__init__(message, status_code=403)


class BookStackNotFoundError(BookStackAPIError):
    """Raised when a resource is not found (404 Not Found)."""

    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, status_code=404)


class BookStackValidationError(BookStackAPIError):
    """Raised when request data is invalid (422 Unprocessable Entity)."""

    def __init__(
        self,
        message: str = "Validation failed",
        validation_errors: dict[str, list[str]] | None = None
    ) -> None:
        super().__init__(message, status_code=422)
        self.validation_errors = validation_errors or {}

    @property
    def field_errors(self) -> dict[str, list[str]]:
        """Get field-specific validation errors."""
        if isinstance(self.response_data, dict):
            errors = self.response_data.get("error", {}).get("validation", {})
            if isinstance(errors, dict):
                return errors
        return self.validation_errors


class BookStackRateLimitError(BookStackAPIError):
    """Raised when rate limit is exceeded (429 Too Many Requests)."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        retry_after: int | None = None
    ) -> None:
        super().__init__(message, status_code=429)
        self.retry_after = retry_after


class BookStackServerError(BookStackAPIError):
    """Raised when the server returns a 5xx error."""

    def __init__(self, message: str = "Internal server error", status_code: int = 500) -> None:
        super().__init__(message, status_code=status_code)


def create_api_error(response: httpx.Response) -> BookStackAPIError:
    """Create the appropriate API error based on response status code.

    Args:
        response: The HTTP response object

    Returns:
        Appropriate BookStackAPIError subclass instance
    """
    status_code = response.status_code
    request_url = str(response.request.url)
    request_method = response.request.method

    # Try to parse response JSON
    response_data: dict[str, Any] = {}
    try:
        response_data = response.json()
    except Exception:
        pass

    # Extract error message
    error_message = "API request failed"
    if response_data:
        # Try different possible error message fields
        for field in ["message", "error", "detail", "title"]:
            if field in response_data:
                error_message = str(response_data[field])
                break
        # Handle nested error structure
        if "error" in response_data and isinstance(response_data["error"], dict):
            error_obj = response_data["error"]
            for field in ["message", "detail", "description"]:
                if field in error_obj:
                    error_message = str(error_obj[field])
                    break

    # If no specific message found, use response text
    if error_message == "API request failed" and response.text:
        error_message = f"API request failed: {response.text[:200]}"

    # Create specific exception based on status code
    if status_code == 401:
        return BookStackAuthenticationError(error_message)
    elif status_code == 403:
        return BookStackPermissionError(error_message)
    elif status_code == 404:
        return BookStackNotFoundError(error_message)
    elif status_code == 422:
        validation_errors = {}
        if "error" in response_data and "validation" in response_data["error"]:
            validation_errors = response_data["error"]["validation"]
        return BookStackValidationError(error_message, validation_errors)
    elif status_code == 429:
        retry_after = None
        if "retry-after" in response.headers:
            try:
                retry_after = int(response.headers["retry-after"])
            except ValueError:
                pass
        return BookStackRateLimitError(error_message, retry_after)
    elif 500 <= status_code < 600:
        return BookStackServerError(error_message, status_code)
    else:
        return BookStackAPIError(
            error_message,
            status_code=status_code,
            response_data=response_data,
            request_url=request_url,
            request_method=request_method,
        )


def create_connection_error(error: httpx.RequestError) -> BookStackError:
    """Create appropriate connection error based on the underlying error.

    Args:
        error: The original httpx RequestError

    Returns:
        Appropriate BookStackError subclass instance
    """
    if isinstance(error, httpx.TimeoutException):
        timeout_value = None
        if hasattr(error, 'request') and hasattr(error.request, 'timeout'):
            timeout_value = getattr(error.request.timeout, 'read', None)
        return BookStackTimeoutError("Request timed out", timeout_value)
    elif isinstance(error, (httpx.ConnectError, httpx.NetworkError)):
        return BookStackConnectionError(f"Connection failed: {error}")
    else:
        return BookStackError(f"Request error: {error}", original_error=error)
