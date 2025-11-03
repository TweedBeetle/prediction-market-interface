---
url: https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug
title: Get tags related to a tag slug - Polymarket Documentation
scraped_at: 2025-11-03T15:03:55.148510
---

[Skip to main content](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Tags

Get tags related to a tag slug

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get tags related to a tag slug

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags/slug/{slug}/related-tags/tags

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

/

slug

/

{slug}

/

related-tags

/

tags

Try it

Get tags related to a tag slug

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags/slug/{slug}/related-tags/tags

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

#### Path Parameters

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#parameter-slug)

slug

string

required

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#parameter-omit-empty)

omit\_empty

boolean

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#parameter-status)

status

enum<string>

Available options:

`active`,

`closed`,

`all`

#### Response

200 - application/json

Related tags

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-label)

label

string | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-force-show)

forceShow

boolean | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-published-at)

publishedAt

string | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-created-by)

createdBy

integer | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-updated-by)

updatedBy

integer | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-force-hide)

forceHide

boolean | null

[​](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug#response-is-carousel)

isCarousel

boolean | null

[Get tags related to a tag id](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id)
[List events](https://docs.polymarket.com/api-reference/events/list-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.