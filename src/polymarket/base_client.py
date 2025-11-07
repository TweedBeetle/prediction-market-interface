"""
Base HTTP client for Polymarket APIs.

Provides common functionality for GammaClient and ClobClient including:
- HTTP request handling
- Error handling
- Rate limiting
- Logging
"""

import asyncio
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import httpx
from loguru import logger


class PolymarketAPIError(Exception):
    """Base exception for Polymarket API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None, response_data: Optional[Dict] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data


class RateLimitError(PolymarketAPIError):
    """Raised when rate limit is exceeded."""
    pass


class AuthenticationError(PolymarketAPIError):
    """Raised when authentication fails."""
    pass


class MarketNotFoundError(PolymarketAPIError):
    """Raised when a market is not found."""
    pass


class OrderError(PolymarketAPIError):
    """Raised when an order operation fails."""
    pass


class BaseClient:
    """
    Base HTTP client for Polymarket APIs.

    Provides common HTTP functionality and error handling.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        max_retries: int = 3,
        rate_limit_calls: int = 100,
        rate_limit_period: int = 60,
    ):
        """
        Initialize base client.

        Args:
            base_url: Base URL for the API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            rate_limit_calls: Maximum calls per period
            rate_limit_period: Rate limit period in seconds
        """
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries

        # Rate limiting
        self.rate_limit_calls = rate_limit_calls
        self.rate_limit_period = rate_limit_period
        self._rate_limit_tokens = rate_limit_calls
        self._rate_limit_last_reset = asyncio.get_event_loop().time()

        # HTTP client (created in context manager)
        self._client: Optional[httpx.AsyncClient] = None

        logger.info(f"Initialized BaseClient for {base_url}")

    async def __aenter__(self):
        """Async context manager entry."""
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self._get_default_headers(),
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._client:
            await self._client.aclose()

    def _get_default_headers(self) -> Dict[str, str]:
        """
        Get default headers for requests.

        Can be overridden by subclasses to add authentication headers.
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def _check_rate_limit(self):
        """
        Check and enforce rate limits.

        Raises:
            RateLimitError: If rate limit is exceeded
        """
        current_time = asyncio.get_event_loop().time()
        time_since_reset = current_time - self._rate_limit_last_reset

        # Reset tokens if period has elapsed
        if time_since_reset >= self.rate_limit_period:
            self._rate_limit_tokens = self.rate_limit_calls
            self._rate_limit_last_reset = current_time

        # Check if we have tokens available
        if self._rate_limit_tokens <= 0:
            wait_time = self.rate_limit_period - time_since_reset
            raise RateLimitError(
                f"Rate limit exceeded. Please wait {wait_time:.1f} seconds.",
                status_code=429
            )

        # Consume a token
        self._rate_limit_tokens -= 1

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request with error handling and retries.

        Args:
            method: HTTP method (GET, POST, DELETE, etc.)
            endpoint: API endpoint path
            params: Query parameters
            json_data: JSON body data
            headers: Additional headers

        Returns:
            Response data as dictionary

        Raises:
            PolymarketAPIError: On API errors
            RateLimitError: On rate limit exceeded
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use 'async with' context manager.")

        # Check rate limit
        await self._check_rate_limit()

        # Merge headers
        request_headers = self._get_default_headers()
        if headers:
            request_headers.update(headers)

        # Build full URL
        url = endpoint if endpoint.startswith("http") else urljoin(self.base_url, endpoint)

        # Retry logic
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                logger.debug(f"{method} {url} (attempt {attempt + 1}/{self.max_retries})")

                response = await self._client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json_data,
                    headers=request_headers,
                )

                # Handle response
                return await self._handle_response(response)

            except httpx.HTTPStatusError as e:
                last_exception = e
                if e.response.status_code == 429:
                    # Rate limit - don't retry
                    raise RateLimitError(
                        "Rate limit exceeded",
                        status_code=429,
                        response_data=e.response.json() if e.response.content else None
                    )
                elif e.response.status_code in [500, 502, 503, 504]:
                    # Server error - retry
                    if attempt < self.max_retries - 1:
                        wait_time = 2 ** attempt  # Exponential backoff
                        logger.warning(f"Server error {e.response.status_code}, retrying in {wait_time}s...")
                        await asyncio.sleep(wait_time)
                        continue
                # Other errors - raise immediately
                raise

            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt
                    logger.warning(f"Network error, retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)
                    continue
                raise PolymarketAPIError(f"Network error: {str(e)}")

        # If we get here, all retries failed
        raise PolymarketAPIError(f"Request failed after {self.max_retries} attempts: {str(last_exception)}")

    async def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """
        Handle HTTP response and raise appropriate errors.

        Args:
            response: HTTP response

        Returns:
            Response data as dictionary

        Raises:
            PolymarketAPIError: On API errors
        """
        # Raise for HTTP errors
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            # Try to extract error message from response
            error_data = None
            error_message = f"HTTP {e.response.status_code}"

            try:
                error_data = e.response.json()
                if isinstance(error_data, dict):
                    error_message = error_data.get("error", error_data.get("message", error_message))
            except Exception:
                error_message = e.response.text[:200] if e.response.text else error_message

            # Raise specific errors based on status code
            if e.response.status_code == 401 or e.response.status_code == 403:
                raise AuthenticationError(
                    f"Authentication failed: {error_message}",
                    status_code=e.response.status_code,
                    response_data=error_data
                )
            elif e.response.status_code == 404:
                raise MarketNotFoundError(
                    f"Resource not found: {error_message}",
                    status_code=404,
                    response_data=error_data
                )
            elif e.response.status_code == 429:
                raise RateLimitError(
                    "Rate limit exceeded",
                    status_code=429,
                    response_data=error_data
                )
            else:
                raise PolymarketAPIError(
                    error_message,
                    status_code=e.response.status_code,
                    response_data=error_data
                )

        # Parse JSON response
        try:
            return response.json()
        except Exception as e:
            logger.error(f"Failed to parse JSON response: {e}")
            return {"raw_response": response.text}

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Make a GET request."""
        return await self._request("GET", endpoint, params=params, headers=headers)

    async def post(
        self,
        endpoint: str,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Make a POST request."""
        return await self._request("POST", endpoint, json_data=json_data, headers=headers)

    async def delete(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Make a DELETE request."""
        return await self._request("DELETE", endpoint, params=params, headers=headers)
