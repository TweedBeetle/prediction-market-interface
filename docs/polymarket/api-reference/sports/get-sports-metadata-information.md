---
url: https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information
title: Get sports metadata information - Polymarket Documentation
description: Retrieves metadata for various sports including images, resolution sources, ordering preferences, tags, and series information. This endpoint provides comprehensive sport configuration data used throughout the platform.
scraped_at: 2025-11-03T15:03:51.109491
---

[Skip to main content](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Sports

Get sports metadata information

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get sports metadata information

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/sports

200

Copy

Ask AI

    [\
      {\
        "sport": "<string>",\
        "image": "<string>",\
        "resolution": "<string>",\
        "ordering": "<string>",\
        "tags": "<string>",\
        "series": "<string>"\
      }\
    ]

GET

/

sports

Try it

Get sports metadata information

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/sports

200

Copy

Ask AI

    [\
      {\
        "sport": "<string>",\
        "image": "<string>",\
        "resolution": "<string>",\
        "ordering": "<string>",\
        "tags": "<string>",\
        "series": "<string>"\
      }\
    ]

#### Response

200 - application/json

List of sports metadata objects containing sport configuration details, visual assets, and related identifiers

[​](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#response-sport)

sport

string

The sport identifier or abbreviation

[​](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#response-image)

image

string<uri>

URL to the sport's logo or image asset

[​](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#response-resolution)

resolution

string<uri>

URL to the official resolution source for the sport (e.g., league website)

[​](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#response-ordering)

ordering

string

Preferred ordering for sport display, typically "home" or "away"

[​](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#response-tags)

tags

string

Comma-separated list of tag IDs associated with the sport for categorization and filtering

[​](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information#response-series)

series

string

Series identifier linking the sport to a specific tournament or season series

[List teams](https://docs.polymarket.com/api-reference/sports/list-teams)
[List tags](https://docs.polymarket.com/api-reference/tags/list-tags)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.