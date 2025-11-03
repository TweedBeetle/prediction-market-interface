---
url: https://docs.polymarket.com/api-reference/tags/list-tags
title: List tags - Polymarket Documentation
scraped_at: 2025-11-03T15:03:55.137984
---

[Skip to main content](https://docs.polymarket.com/api-reference/tags/list-tags#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Tags

List tags

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

List tags

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags

200

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

tags

Try it

List tags

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags

200

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

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/tags/list-tags#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/tags/list-tags#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/tags/list-tags#parameter-order)

order

string

Comma-separated list of fields to order by

[​](https://docs.polymarket.com/api-reference/tags/list-tags#parameter-ascending)

ascending

boolean

[​](https://docs.polymarket.com/api-reference/tags/list-tags#parameter-include-template)

include\_template

boolean

[​](https://docs.polymarket.com/api-reference/tags/list-tags#parameter-is-carousel)

is\_carousel

boolean

#### Response

200 - application/json

List of tags

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-label)

label

string | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-force-show)

forceShow

boolean | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-published-at)

publishedAt

string | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-created-by)

createdBy

integer | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-updated-by)

updatedBy

integer | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-force-hide)

forceHide

boolean | null

[​](https://docs.polymarket.com/api-reference/tags/list-tags#response-is-carousel)

isCarousel

boolean | null

[Get sports metadata information](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information)
[Get tag by id](https://docs.polymarket.com/api-reference/tags/get-tag-by-id)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.