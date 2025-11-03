---
url: https://docs.polymarket.com/api-reference/tags/get-tag-by-id
title: Get tag by id - Polymarket Documentation
scraped_at: 2025-11-03T15:03:54.100003
---

[Skip to main content](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Tags

Get tag by id

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get tag by id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags/{id}

200

404

Copy

Ask AI

    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }

GET

/

tags

/

{id}

Try it

Get tag by id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags/{id}

200

404

Copy

Ask AI

    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }

#### Path Parameters

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#parameter-id)

id

integer

required

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#parameter-include-template)

include\_template

boolean

#### Response

200

application/json

Tag

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-label)

label

string | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-force-show)

forceShow

boolean | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-published-at)

publishedAt

string | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-created-by)

createdBy

integer | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-updated-by)

updatedBy

integer | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-force-hide)

forceHide

boolean | null

[​](https://docs.polymarket.com/api-reference/tags/get-tag-by-id#response-is-carousel)

isCarousel

boolean | null

[List tags](https://docs.polymarket.com/api-reference/tags/list-tags)
[Get tag by slug](https://docs.polymarket.com/api-reference/tags/get-tag-by-slug)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.