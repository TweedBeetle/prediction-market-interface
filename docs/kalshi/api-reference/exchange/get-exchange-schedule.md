---
url: https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule
title: Get Exchange Schedule - API Documentation
description:  Endpoint for getting the exchange schedule.
scraped_at: 2025-11-03T14:46:16.263352
---

[Skip to main content](https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

exchange

Get Exchange Schedule

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Exchange Schedule

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/schedule

200

500

Copy

Ask AI

    {
      "schedule": {
        "standard_hours": [\
          {\
            "start_time": "2023-11-07T05:31:56Z",\
            "end_time": "2023-11-07T05:31:56Z",\
            "monday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "tuesday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "wednesday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "thursday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "friday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "saturday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "sunday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ]\
          }\
        ],
        "maintenance_windows": [\
          {\
            "start_datetime": "2023-11-07T05:31:56Z",\
            "end_datetime": "2023-11-07T05:31:56Z"\
          }\
        ]
      }
    }

GET

/

exchange

/

schedule

Try it

Get Exchange Schedule

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/schedule

200

500

Copy

Ask AI

    {
      "schedule": {
        "standard_hours": [\
          {\
            "start_time": "2023-11-07T05:31:56Z",\
            "end_time": "2023-11-07T05:31:56Z",\
            "monday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "tuesday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "wednesday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "thursday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "friday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "saturday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ],\
            "sunday": [\
              {\
                "open_time": "<string>",\
                "close_time": "<string>"\
              }\
            ]\
          }\
        ],
        "maintenance_windows": [\
          {\
            "start_datetime": "2023-11-07T05:31:56Z",\
            "end_datetime": "2023-11-07T05:31:56Z"\
          }\
        ]
      }
    }

#### Response

200

application/json

Exchange schedule retrieved successfully

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule#response-schedule)

schedule

object

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule#response-schedule-standard-hours)

schedule.standard\_hours

object\[\]

required

The standard operating hours of the exchange. All times are expressed in ET. Outside of these times trading will be unavailable.

Show child attributes

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule#response-schedule-maintenance-windows)

schedule.maintenance\_windows

object\[\]

required

Scheduled maintenance windows, during which the exchange may be unavailable.

Show child attributes

[Get Series Fee Changes](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes)
[Get User Data Timestamp](https://docs.kalshi.com/api-reference/exchange/get-user-data-timestamp)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.