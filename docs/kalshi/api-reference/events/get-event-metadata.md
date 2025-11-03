---
url: https://docs.kalshi.com/api-reference/events/get-event-metadata
title: Get Event Metadata - API Documentation
description:  Endpoint for getting metadata about an event by its ticker.  Returns only the metadata information for an event.
scraped_at: 2025-11-03T14:46:15.491544
---

[Skip to main content](https://docs.kalshi.com/api-reference/events/get-event-metadata#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

events

Get Event Metadata

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Event Metadata

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/events/{event_ticker}/metadata

200

400

401

404

500

Copy

Ask AI

    {
      "image_url": "<string>",
      "settlement_sources": [\
        {\
          "name": "<string>",\
          "url": "<string>"\
        }\
      ],
      "competition": "<string>",
      "competition_scope": "<string>"
    }

GET

/

events

/

{event\_ticker}

/

metadata

Try it

Get Event Metadata

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/events/{event_ticker}/metadata

200

400

401

404

500

Copy

Ask AI

    {
      "image_url": "<string>",
      "settlement_sources": [\
        {\
          "name": "<string>",\
          "url": "<string>"\
        }\
      ],
      "competition": "<string>",
      "competition_scope": "<string>"
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#parameter-event-ticker)

event\_ticker

string

required

Event ticker

#### Response

200

application/json

Event metadata retrieved successfully

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#response-image-url)

image\_url

string

required

A path to an image that represents this event.

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#response-settlement-sources)

settlement\_sources

object\[\]

required

A list of settlement sources for this event.

Show child attributes

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#response-settlement-sources-name)

name

string

Name of the settlement source

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#response-settlement-sources-url)

url

string

URL to the settlement source

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#response-competition)

competition

string | null

Event competition.

[​](https://docs.kalshi.com/api-reference/events/get-event-metadata#response-competition-scope)

competition\_scope

string | null

Event scope, based on the competition.

[Get Event](https://docs.kalshi.com/api-reference/events/get-event)
[Get Event Forecast Percentile History](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.