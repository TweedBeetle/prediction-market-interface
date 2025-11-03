---
url: https://docs.polymarket.com/api-reference/sports/list-teams
title: List teams - Polymarket Documentation
scraped_at: 2025-11-03T15:03:51.352086
---

[Skip to main content](https://docs.polymarket.com/api-reference/sports/list-teams#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Sports

List teams

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

List teams

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/teams

200

Copy

Ask AI

    [\
      {\
        "id": 123,\
        "name": "<string>",\
        "league": "<string>",\
        "record": "<string>",\
        "logo": "<string>",\
        "abbreviation": "<string>",\
        "alias": "<string>",\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z"\
      }\
    ]

GET

/

teams

Try it

List teams

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/teams

200

Copy

Ask AI

    [\
      {\
        "id": 123,\
        "name": "<string>",\
        "league": "<string>",\
        "record": "<string>",\
        "logo": "<string>",\
        "abbreviation": "<string>",\
        "alias": "<string>",\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z"\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-order)

order

string

Comma-separated list of fields to order by

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-ascending)

ascending

boolean

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-league)

league

string\[\]

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-name)

name

string\[\]

[​](https://docs.polymarket.com/api-reference/sports/list-teams#parameter-abbreviation)

abbreviation

string\[\]

#### Response

200 - application/json

List of teams

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-id)

id

integer

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-name)

name

string | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-league)

league

string | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-record)

record

string | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-logo)

logo

string | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-abbreviation)

abbreviation

string | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-alias)

alias

string | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/sports/list-teams#response-updated-at)

updatedAt

string<date-time> | null

[Health check](https://docs.polymarket.com/api-reference/health/health-check)
[Get sports metadata information](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.