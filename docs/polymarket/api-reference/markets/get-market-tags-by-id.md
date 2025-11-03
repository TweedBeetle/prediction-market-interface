---
url: https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id
title: Get market tags by id - Polymarket Documentation
scraped_at: 2025-11-03T15:03:44.509147
---

[Skip to main content](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Markets

Get market tags by id

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get market tags by id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/markets/{id}/tags

200

404

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "label": "<string>",\
        "slug": "<string>",\
        "forceShow": true,\
        "publishedAt": "<string>",\
        "createdBy": 123,\
        "updatedBy": 123,\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z",\
        "forceHide": true,\
        "isCarousel": true\
      }\
    ]

GET

/

markets

/

{id}

/

tags

Try it

Get market tags by id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/markets/{id}/tags

200

404

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "label": "<string>",\
        "slug": "<string>",\
        "forceShow": true,\
        "publishedAt": "<string>",\
        "createdBy": 123,\
        "updatedBy": 123,\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z",\
        "forceHide": true,\
        "isCarousel": true\
      }\
    ]

#### Path Parameters

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#parameter-id)

id

integer

required

#### Response

200

application/json

Tags attached to the market

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-label)

label

string | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-force-show)

forceShow

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-published-at)

publishedAt

string | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-created-by)

createdBy

integer | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-updated-by)

updatedBy

integer | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-force-hide)

forceHide

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id#response-is-carousel)

isCarousel

boolean | null

[Get market by id](https://docs.polymarket.com/api-reference/markets/get-market-by-id)
[Get market by slug](https://docs.polymarket.com/api-reference/markets/get-market-by-slug)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.