---
url: https://docs.kalshi.com/api-reference/structured-targets/get-structured-target
title: Get Structured Target - API Documentation
description:  Endpoint for getting data about a specific structured target by its ID.
scraped_at: 2025-11-03T14:46:32.975578
---

[Skip to main content](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

structured-targets

Get Structured Target

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Structured Target

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/structured_targets/{structured_target_id}

200

401

404

500

Copy

Ask AI

    {
      "structured_target": {
        "id": "<string>",
        "name": "<string>",
        "type": "<string>",
        "details": {},
        "source_id": "<string>",
        "last_updated_ts": "2023-11-07T05:31:56Z"
      }
    }

GET

/

structured\_targets

/

{structured\_target\_id}

Try it

Get Structured Target

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/structured_targets/{structured_target_id}

200

401

404

500

Copy

Ask AI

    {
      "structured_target": {
        "id": "<string>",
        "name": "<string>",
        "type": "<string>",
        "details": {},
        "source_id": "<string>",
        "last_updated_ts": "2023-11-07T05:31:56Z"
      }
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#parameter-structured-target-id)

structured\_target\_id

string

required

Structured target ID

#### Response

200

application/json

Structured target retrieved successfully

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target)

structured\_target

object

Show child attributes

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target-id)

structured\_target.id

string

Unique identifier for the structured target.

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target-name)

structured\_target.name

string

Name of the structured target.

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target-type)

structured\_target.type

string

Type of the structured target.

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target-details)

structured\_target.details

object

Additional details about the structured target. Contains flexible JSON data specific to the target type.

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target-source-id)

structured\_target.source\_id

string

External source identifier for the structured target, if available (e.g., third-party data provider ID).

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target#response-structured-target-last-updated-ts)

structured\_target.last\_updated\_ts

string<date-time>

Timestamp when this structured target was last updated.

[Get Structured Targets](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets)
[Get Milestone](https://docs.kalshi.com/api-reference/milestone/get-milestone)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.