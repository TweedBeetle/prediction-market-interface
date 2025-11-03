---
url: https://docs.kalshi.com/changelog
title: API Changelog - API Documentation
description: Stay updated with API changes and version history
scraped_at: 2025-11-03T14:46:32.694869
---

[Skip to main content](https://docs.kalshi.com/changelog#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Changelog

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

FiltersClear

UpcomingReleasedBreaking ChangeNew FeatureBug FixDocumentationBreaking changeSDK

You can subscribe to the RSS changelog at `/changelog.rss` if you’d like to stay ahead of breaking changes. You can reference the pending API spec under the “version” dropdown menu at the top left. When the actual API is upgraded to this new version, you will see the version marked as “Stable” in the drop-down menu and become the new default on the landing page. This changelog is a work in progress. As always, we welcome any feedback in our Discord #dev channel!

[​](https://docs.kalshi.com/changelog#recent-updates)

Recent Updates
-----------------------------------------------------------------------

[​](https://docs.kalshi.com/changelog#oct-31%2C-2025)

Oct 31, 2025

Breaking ChangeUpcoming

Standardized market status values across the API to eliminate confusion between filter parameters and response values. The `status` field in market responses now returns user-facing values that match the filter vocabulary.**Breaking Change:** Market responses will return different status values:

*   `"initialized"` → `"unopened"` (market hasn’t started trading yet)
*   `"active"` → `"open"` (market is currently tradeable)
*   `"determined"` → `"closed"` (market has a result but isn’t settled yet)
*   `"settled"` remains `"settled"` (final result applied, positions settled)

**Affected Endpoints:**

*   `GET /markets` - returns markets with new status values
*   `GET /markets/{ticker}` - returns market with new status value
*   `GET /events` (with `with_nested_markets=true`) - returns events with nested markets using new status values
*   `GET /events/{event_ticker}` - returns event with markets using new status values
*   Any endpoint returning Market objects

[​](https://docs.kalshi.com/changelog#nov-6%2C-2025)

Nov 6, 2025

New FeatureUpcoming

Added comprehensive support for multivariate events (combos) with new API endpoints and enhanced filtering:**New Endpoint and deprecation of multivariate events in GetEvents endpoint**

*   `GET /events/multivariate` - Retrieve multivariate events with filtering by series and collection ticker.
*   `GET /events` will EXCLUDE multivariate events upon the next release (November 13th). Please use the new endpoint!

**Enhanced Market Filtering:**

*   `GET /markets` now supports `mve_filter` parameter:
    *   `"only"` - Returns only multivariate events
    *   `"exclude"` - Excludes multivariate events
    *   No parameter - Returns all events (default behavior)

Expected release: `November 6th, 2025`

[​](https://docs.kalshi.com/changelog#oct-24%2C-2025)

Oct 24, 2025

Bug FixUpcoming

Fixed batch order creation to return proper error details when post-only orders cross the market. The response now includes:

*   Error code: `"invalid order"`
*   Error details: `"post only cross"`

This makes the batch endpoint consistent with single order creation and provides clear feedback on why post-only orders were rejected.

[​](https://docs.kalshi.com/changelog#oct-20%2C-2025)

Oct 20, 2025

Upcoming

The `GET /portfolio/orders` endpoint’s `event_ticker` parameter now supports filtering by multiple events using comma-separated values.**Example usage:**

Copy

Ask AI

    GET /portfolio/orders?event_ticker=EVENT1,EVENT2,EVENT3
    

**Backward Compatible:**

*   Single event ticker queries continue to work as before
*   Multiple event tickers return orders from all specified events

[​](https://docs.kalshi.com/changelog#oct-19%2C-2025)

Oct 19, 2025

Bug FixUpcoming

Fixed missing fields in Quote responses: `rfq_target_cost_centi_cents`, `rfq_creator_order_id`, and `creator_order_id` are now properly included in all Quote-related endpoints.

[​](https://docs.kalshi.com/changelog#oct-16%2C-2025)

Oct 16, 2025

Upcoming

The `GET /events` endpoint now supports an optional flag, `with_milestones`, that includes all milestones related to the returned events.Expected release: `October 16, 2025`

[​](https://docs.kalshi.com/changelog#oct-14%2C-2025)

Oct 14, 2025

Upcoming

The order returned by create order is now the same model as the model returned by get order.

[​](https://docs.kalshi.com/changelog#oct-13%2C-2025)

Oct 13, 2025

Upcoming

The `GET /v2/incentive_programs` and `GET /incentive_programs` endpoints now return a `series_ticker` field for each incentive program.Expected release: `October 13, 2025`

[​](https://docs.kalshi.com/changelog#oct-10%2C-2025)

Oct 10, 2025

Breaking ChangeUpcoming

The `price_level_structure` field has been moved from the event level to the market level. Each market now has its own `price_level_structure` field.**Affected endpoints:**

*   `GET /trade-api/v2/events`
*   `GET /trade-api/v2/events/:event_ticker`
*   `GET /trade-api/v2/markets`
*   `GET /trade-api/v2/markets/:ticker`

**Note:** The `price_level_structure` field on event objects is now deprecated and will be removed. Please use the field on individual market objects instead.Expected release date: `Oct 15th, 2025`

[​](https://docs.kalshi.com/changelog#oct-13%2C-2025-2)

Oct 13, 2025

Bug FixBreaking ChangeUpcoming

Fixed the `GET /series` endpoint’s tags parameter to properly support tags containing spaces. Previously, the parameter would split on both commas AND spaces, breaking searches for tags like “Rotten Tomatoes”.**Breaking Change:**

*   The `tags` query parameter now **only** splits on commas (`,`), not spaces
*   Tags with spaces (e.g., “Rotten Tomatoes”) now work correctly
*   Multiple tags must be comma-separated: `?tags=Rotten Tomatoes,Television`

**Before (broken):**

Copy

Ask AI

    GET /series?tags=Rotten Tomatoes
    // Was incorrectly parsed as: ["Rotten", "Tomatoes"]
    // Result: No matches found
    

**After (fixed):**

Copy

Ask AI

    GET /series?tags=Rotten Tomatoes
    // Correctly parsed as: ["Rotten Tomatoes"]
    // Result: Returns series with the "Rotten Tomatoes" tag
    
    GET /series?tags=Rotten Tomatoes,Television
    // Correctly parsed as: ["Rotten Tomatoes", "Television"]
    // Result: Returns series with either tag
    

This change may affect integrations that relied on space-separated tags. Please update to use comma-separated tags only.

[​](https://docs.kalshi.com/changelog#oct-8%2C-2025)

Oct 8, 2025

Bug FixUpcoming

Fixed routing inconsistency where certain collection endpoints required trailing slashes, causing unnecessary 301 redirects for requests without them.**Endpoints now returning 200 for requests without trailing slash** (previously returned 301):

*   `GET /milestones`
*   `GET /structured_targets`
*   `GET /multivariate_event_collections`
*   `GET /series`
*   `GET /api_keys`
*   `POST /api_keys`

**Note:** Requests with trailing slashes (e.g., `/milestones/`) will now receive a 301 redirect to the version without the trailing slash, which is the opposite of the previous behavior.

[​](https://docs.kalshi.com/changelog#oct-9%2C-2025)

Oct 9, 2025

Upcoming

Subpenny fields have been added to orders (`taker_fees_dollars`, `maker_fees_dollars`), as well as to public trades (`yes_price_dollars`, `no_price_dollars`).Endpoints affected:

*   `GET /trade-api/v2/portfolio/orders`
*   `GET /trade-api/v2/markets/trades`

[​](https://docs.kalshi.com/changelog#oct-9%2C-2025-2)

Oct 9, 2025

Upcoming

Fields have been added to all RFQ and quote messages to support subpenny pricing via the dollar normalized price fields. For more info reference:

*   [Subpenny Pricing](https://docs.kalshi.com/getting_started/subpenny_pricing)
    
*   [Websocket Documentation](https://docs.kalshi.com/api-reference/websockets/communications)
    

[​](https://docs.kalshi.com/changelog#oct-7%2C-2025)

Oct 7, 2025

Upcoming

Enhanced the existing `GET /portfolio/balance` endpoint to include a `portfolio_value` field that provides the total portfolio value (available balance plus current market value of all positions), both in cents.

[​](https://docs.kalshi.com/changelog#oct-1%2C-2025)

Oct 1, 2025

Upcoming

The `GET /series/fee_changes` endpoint now returns user-facing fee type names (`quadratic`, `quadratic_with_maker_fees`, `flat`) instead of internal fee structure names. This change also applies to CustomerIO notifications for scheduled series fee updates.Expected release: `October 1, 2025`

[​](https://docs.kalshi.com/changelog#sep-25%2C-2025)

Sep 25, 2025

Upcoming

Repeated subscriptions on the same websocket call will no longer error. If passing the same market tickers as before, no action will be taken. If passing new market tickers, they will be added to your existing subscription.Additionally, the user may supply WS Command `list_subscriptions` to view their existing subscriptions.Expected release: `October 1, 2025`

[​](https://docs.kalshi.com/changelog#sep-25%2C-2025-2)

Sep 25, 2025

Upcoming

For optimization purposes, partial fills generated by self-crossing FoK orders are not rolled back. If a FoK order self-crosses, order execution proceeds based on `self_trade_prevention_type`:

*   `taker_at_cross`: the taker is canceled, execution stops. Any partial fills are executed.
*   `maker`: the maker is canceled, execution continues. After execution, remaining taker quantity is canceled. Any fills are executed.

This fixes a bug where partially filled FoK orders with Maker STP entered into the book after self-crossing. Expected enforced date: `Oct 1, 2025`.

[​](https://docs.kalshi.com/changelog#sep-22%2C-2025)

Sep 22, 2025

Upcoming

User seeking a simple way to determine the direction of their fill should reference purchased\_side. Both BUY YES or SELL NO result in purchased\_side = YES. The addition of this field is the first step in standardizing the fills websocket and REST endpoints, which have different conventions for the interpretation ‘side’ and ‘user\_action’.Expected Enforce Date: deprecation date for existing fields not yet scheduled.

[​](https://docs.kalshi.com/changelog#sep-21%2C-2025)

Sep 21, 2025

Upcoming

Added new public API endpoint for getting all of a series’ scheduled fees:

*   `GET /series/fee_changes` - Get a series’ fee changes. If query string parameter show\_historical is set to true, ALL fee changes previous and upcoming will be shown. If set to false, only upcoming fee changes will be shown

[​](https://docs.kalshi.com/changelog#sep-25%2C-2025-3)

Sep 25, 2025

UpcomingBreaking Change

Specifying `order_type` is no longer required and only `limit` type orders will be supported. Price must be supplied based on the underlying market structure. Example usage:

Copy

Ask AI

    {"yes_price": 99, "side: "yes"} // buy yes or sell no at market price
    {"no_price": 99, "side: "no"} // buy no or sell yes at market price
    

Expected enforce date: `Sep 25, 2025`

[​](https://docs.kalshi.com/changelog#sep-18%2C-2025)

Sep 18, 2025

Breaking changeUpcoming

WebSocket connections per user are limited by usage tier. The default limit begins at 200 and increases based on API usage tier.

[​](https://docs.kalshi.com/changelog#sep-18%2C-2025-2)

Sep 18, 2025

Upcoming

A new WS channel is being introduced for streaming information related to pre-trade communications (RFQs and quotes).

[​](https://docs.kalshi.com/changelog#sep-15%2C-2025)

Sep 15, 2025

Upcoming

Additional metadata is being added to RFQs on multivarate events (MVEs) that break down their component parts explicitly. Market payloads are also being expanded with these new optional fields that are filled only for MVE markets.

[​](https://docs.kalshi.com/changelog#sep-15%2C-2025-2)

Sep 15, 2025

Upcoming

Added new public API endpoint for event candlesticks:

*   `GET /candlesticks` - Get candlesticks for all markets associated with an event. If the # of candlesticks exceeds 5000, paginate the results and return an adjustedEndTs which should be used as the start\_ts for your next request.

[​](https://docs.kalshi.com/changelog#sept-11%2C-2025)

Sept 11, 2025

SDKReleased

The TypeScript SDK is now available through NPM! Install with `npm install kalshi-typescript`.Documentation and examples available at docs.kalshi.com

[​](https://docs.kalshi.com/changelog#sep-11%2C-2025)

Sep 11, 2025

Upcoming

Added new public API endpoint for forecast percentiles history:

*   `GET /forecast_percentiles_history` - Get percentile history of a event forecast

[​](https://docs.kalshi.com/changelog#sep-10%2C-2025)

Sep 10, 2025

Upcoming

Added new public API endpoint for incentive programs (not yet live):

*   `GET /incentive_programs` - List incentive programs with filtering options (by market ticker, active status, payout status)

[​](https://docs.kalshi.com/changelog#sep-9%2C-2025)

Sep 9, 2025

Upcoming

Subpenny pricing fields have been added to websocket messages. Any message bearing price in cents will now also bear an equivalent fixed-point dollars field.For more info, see [Subpenny Pricing](https://docs.kalshi.com/getting_started/subpenny_pricing)
.

[​](https://docs.kalshi.com/changelog#sep-9%2C-2025-2)

Sep 9, 2025

Upcoming

Both the individual and batch `GET` events endpoints now also return `available_on_brokers` which indicates that they are available on intermediate platforms/ brokers.

[​](https://docs.kalshi.com/changelog#sep-6%2C-2025)

Sep 6, 2025

Breaking ChangeReleased

The python SDK is being generated from our OpenAPI spec and is available through pip with pip install kalshi-python. Docs for the new SDK are available on docs.kalshi.com/python-sdk.

[​](https://docs.kalshi.com/changelog#aug-31%2C-2025)

Aug 31, 2025

Breaking ChangeUpcoming

Subpenny pricing fields have been added to APIs involving price, fees, and money in general. E.g. next to a field called `"price": 12` (representing 12 cents), you will also see `"price_dollars": "0.1200"`, which is a string bearing a fixed-point representation of money accuate to at 4 decimal points.For now, this change is read-only, meaning that the minimum allowable tick size for orders is still 1c. Eventually, we will introduce sub-penny pricing on orders. For now, please prepare for an eventual migration to the higher granularity price representation.For more info, see [Subpenny Pricing](https://docs.kalshi.com/getting_started/subpenny_pricing)
.

[​](https://docs.kalshi.com/changelog#sep-2%2C-2025)

Sep 2, 2025

Released

The market payload has been updated to include two new fields that describe markets which are part of Multivariate Events.

[​](https://docs.kalshi.com/changelog#sep-2%2C-2025-2)

Sep 2, 2025

Released

The market payload has been updated to include two new fields that describe markets which are part of Multivariate Events.

[​](https://docs.kalshi.com/changelog#aug-21%2C-2025)

Aug 21, 2025

Released

The MVE payload has been expanded to support more flexible structures. Several fields that are now redundant are deprecated, but not yet removed.

[​](https://docs.kalshi.com/changelog#aug-21%2C-2025-2)

Aug 21, 2025

New FeatureReleased

The Settlements API now includes the settlement value for a yes contract.

[​](https://docs.kalshi.com/changelog#aug-21%2C-2025-3)

Aug 21, 2025

Bug FixReleased

The get\_milestones endpoint now uses case-insensitive matching for the category parameter, resolving inconsistent filtering behavior between “Sports” and “sports”.

[​](https://docs.kalshi.com/changelog#aug-14%2C-2025)

Aug 14, 2025

New FeatureReleased

Filtering events by close ts and series by tags supported in the API.

[​](https://docs.kalshi.com/changelog#aug-13%2C-2025)

Aug 13, 2025

Released

The batch order endpoints are now available to all API users in the demo environment:**Affected Endpoints:**

*   `POST /portfolio/orders/batched` (BatchCreateOrders)
*   `DELETE /portfolio/orders/batched` (BatchCancelOrders)

**Changes:**

*   Basic tier users can now access batch endpoints in demo environment
*   Production environment remains unchanged - Advanced tier or higher still required
*   Rate limits still apply based on user tier

This change enables developers to test batch order functionality without needing Advanced tier access in the demo environment.

[​](https://docs.kalshi.com/changelog#aug-13%2C-2025-2)

Aug 13, 2025

DocumentationReleased

The error messages when an incorrect API signature is passed have been improved

[​](https://docs.kalshi.com/changelog#aug-9%2C-2025)

Aug 9, 2025

DocumentationReleased

The OpenAPI specification for the Kalshi API is now available at `https://docs.kalshi.com/openapi.yaml`. This allows developers to easily generate client libraries and integrate with the API using OpenAPI-compatible tools.

[​](https://docs.kalshi.com/changelog#aug-8%2C-2025)

Aug 8, 2025

ReleasedNew Feature

Added `client_order_id` field to orderbook delta WebSocket messages. This field appears only when you caused the orderbook change and contains the client\_order\_id of your order that triggered the delta.**WebSocket Message Enhancement:**

*   New field: `client_order_id` (string, optional)
*   Present only when the authenticated user’s order causes the orderbook change
*   Contains the client-provided order ID of the triggering order

See the WebSocket documentation for implementation details.

[​](https://docs.kalshi.com/changelog#aug-1%2C-2025)

Aug 1, 2025

ReleasedNew Feature

Added `GET /portfolio/orders/queue_positions` endpoint for retrieving queue positions of multiple resting orders.**Request Parameters:**

*   `market_tickers` (optional): Array of market tickers to filter by
*   `event_ticker` (optional): Event ticker to filter by

Note: You must specify one of `market_tickers` and `event_ticker` in the request.

[​](https://docs.kalshi.com/changelog#july-31%2C-2025)

July 31, 2025

ReleasedBreaking ChangeDocumentation

We are migrating our API documentation to a new platform:

*   **RSS feed moved** from `https://trading-api.readme.io/changelog.rss` to `https://docs.kalshi.com/changelog/rss.xml`
*   **Documentation site** `trading-api.readme.io` is now deprecated
*   **New documentation home**: `https://docs.kalshi.com`
*   Historical changelog entries will not be backfilled to the new RSS feed

Please update your bookmarks and RSS subscriptions.

[​](https://docs.kalshi.com/changelog#july-31%2C-2025-2)

July 31, 2025

Released

The GetEventMetadata endpoint has been expanded to include settlement sources.

[​](https://docs.kalshi.com/changelog#july-29%2C-2025)

July 29, 2025

ReleasedBreaking Change

The GetApiVersion endpoint has been removed. API versioning will not be available for the time being.

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.