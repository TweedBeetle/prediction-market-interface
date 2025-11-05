"""
Gamma API client for Polymarket market data.

Provides read-only access to:
- Market search and details
- Event information
- Price data
- Order book snapshots
- Trade history
"""

from typing import List, Optional

from loguru import logger

from .base_client import BaseClient
from .models import Market, Event, OrderBook, OrderBookLevel, Trade


class GammaClient(BaseClient):
    """
    Client for Polymarket Gamma API (read-only market data).

    The Gamma API provides access to market information, events,
    orderbook snapshots, and trade history without requiring authentication.
    """

    GAMMA_BASE_URL = "https://gamma-api.polymarket.com"

    def __init__(
        self,
        base_url: str = GAMMA_BASE_URL,
        timeout: int = 30,
        max_retries: int = 3,
        rate_limit_calls: int = 100,
        rate_limit_period: int = 60,
    ):
        """
        Initialize Gamma client.

        Args:
            base_url: Base URL for Gamma API
            timeout: Request timeout in seconds
            max_retries: Maximum retries for failed requests
            rate_limit_calls: Max calls per period
            rate_limit_period: Rate limit period in seconds
        """
        super().__init__(base_url, timeout, max_retries, rate_limit_calls, rate_limit_period)
        logger.info("Initialized GammaClient")

    async def search_markets(
        self,
        query: Optional[str] = None,
        active: bool = True,
        closed: bool = False,
        limit: int = 20,
        offset: int = 0,
    ) -> List[Market]:
        """
        Search for markets.

        Args:
            query: Search query (searches title, description)
            active: Include active markets
            closed: Include closed markets
            limit: Maximum number of results
            offset: Pagination offset

        Returns:
            List of matching markets
        """
        params = {
            "limit": limit,
            "offset": offset,
            "active": str(active).lower(),
            "closed": str(closed).lower(),
        }

        if query:
            params["query"] = query

        logger.info(f"Searching markets with query='{query}', limit={limit}")

        try:
            response = await self.get("/markets", params=params)

            # Parse response - Gamma API returns list directly or under "markets" key
            markets_data = response if isinstance(response, list) else response.get("markets", [])

            markets = [Market(**m) for m in markets_data]

            logger.info(f"Found {len(markets)} markets")
            return markets

        except Exception as e:
            logger.error(f"Failed to search markets: {e}")
            raise

    async def get_market(self, market_id: str) -> Market:
        """
        Get detailed market information.

        Args:
            market_id: Market ID or condition ID

        Returns:
            Market data

        Raises:
            MarketNotFoundError: If market not found
        """
        logger.info(f"Fetching market {market_id}")

        try:
            response = await self.get(f"/markets/{market_id}")

            # Response may be direct market object or wrapped
            market_data = response if "id" in response else response.get("market", response)

            market = Market(**market_data)

            logger.info(f"Retrieved market: {market.question}")
            return market

        except Exception as e:
            logger.error(f"Failed to get market {market_id}: {e}")
            raise

    async def get_market_by_slug(self, slug: str) -> Market:
        """
        Get market by URL slug.

        Args:
            slug: Market slug (URL-friendly identifier)

        Returns:
            Market data
        """
        logger.info(f"Fetching market by slug: {slug}")

        try:
            response = await self.get(f"/markets/slug/{slug}")
            market_data = response if "id" in response else response.get("market", response)
            return Market(**market_data)

        except Exception as e:
            logger.error(f"Failed to get market by slug {slug}: {e}")
            raise

    async def get_orderbook(self, token_id: str) -> OrderBook:
        """
        Get orderbook snapshot for a token.

        Note: This endpoint is actually on the CLOB API but doesn't require authentication.
        We proxy it here for convenience since it's market data.

        Args:
            token_id: CLOB token ID (YES or NO outcome)

        Returns:
            Order book data with bids and asks
        """
        logger.info(f"Fetching orderbook for token {token_id}")

        try:
            # Orderbook is on CLOB API, not Gamma API
            # Use a direct HTTP request to CLOB endpoint
            import httpx

            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    "https://clob.polymarket.com/book",
                    params={"token_id": token_id}
                )
                response.raise_for_status()
                data = response.json()

            # Parse orderbook data
            bids_data = data.get("bids", [])
            asks_data = data.get("asks", [])

            bids = [
                OrderBookLevel(price=float(level["price"]), size=float(level["size"]))
                for level in bids_data
            ]
            asks = [
                OrderBookLevel(price=float(level["price"]), size=float(level["size"]))
                for level in asks_data
            ]

            orderbook = OrderBook(
                market_id=data.get("market", ""),
                token_id=token_id,
                bids=bids,
                asks=asks,
                timestamp=data.get("timestamp"),
            )

            logger.info(f"Retrieved orderbook with {len(bids)} bids and {len(asks)} asks")
            return orderbook

        except Exception as e:
            logger.error(f"Failed to get orderbook for token {token_id}: {e}")
            raise

    async def get_events(
        self,
        active: bool = True,
        closed: bool = False,
        limit: int = 20,
        offset: int = 0,
    ) -> List[Event]:
        """
        List events (collections of related markets).

        Args:
            active: Include active events
            closed: Include closed events
            limit: Maximum number of results
            offset: Pagination offset

        Returns:
            List of events
        """
        params = {
            "limit": limit,
            "offset": offset,
            "active": str(active).lower(),
            "closed": str(closed).lower(),
        }

        logger.info(f"Fetching events (limit={limit})")

        try:
            response = await self.get("/events", params=params)

            # Parse events
            events_data = response if isinstance(response, list) else response.get("events", [])

            events = []
            for event_data in events_data:
                try:
                    event = Event(**event_data)
                    events.append(event)
                except Exception as e:
                    logger.warning(f"Failed to parse event: {e}")
                    continue

            logger.info(f"Retrieved {len(events)} events")
            return events

        except Exception as e:
            logger.error(f"Failed to get events: {e}")
            raise

    async def get_event(self, event_id: str) -> Event:
        """
        Get detailed event information.

        Args:
            event_id: Event ID or slug

        Returns:
            Event data with associated markets
        """
        logger.info(f"Fetching event {event_id}")

        try:
            response = await self.get(f"/events/{event_id}")

            event_data = response if "id" in response else response.get("event", response)
            event = Event(**event_data)

            logger.info(f"Retrieved event: {event.title} ({event.market_count} markets)")
            return event

        except Exception as e:
            logger.error(f"Failed to get event {event_id}: {e}")
            raise

    @classmethod
    def from_env(cls) -> "GammaClient":
        """
        Create client from environment variables.

        Returns:
            Configured GammaClient instance
        """
        import os

        base_url = os.getenv("POLYMARKET_GAMMA_URL", cls.GAMMA_BASE_URL)

        return cls(base_url=base_url)
