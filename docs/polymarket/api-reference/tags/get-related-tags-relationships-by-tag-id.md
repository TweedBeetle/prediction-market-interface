---
url: https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id
title: Get related tags (relationships) by tag id - Polymarket Documentation
scraped_at: 2025-11-03T15:03:53.124259
---

[Skip to main content](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Tags

Get related tags (relationships) by tag id

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get related tags (relationships) by tag id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags/{id}/related-tags

200

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "tagID": 123,\
        "relatedTagID": 123,\
        "rank": 123\
      }\
    ]

GET

/

tags

/

{id}

/

related-tags

Try it

Get related tags (relationships) by tag id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/tags/{id}/related-tags

200

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "tagID": 123,\
        "relatedTagID": 123,\
        "rank": 123\
      }\
    ]

#### Path Parameters

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#parameter-id)

id

integer

required

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#parameter-omit-empty)

omit\_empty

boolean

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#parameter-status)

status

enum<string>

Available options:

`active`,

`closed`,

`all`

#### Response

200 - application/json

Related tag relationships

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#response-tag-id)

tagID

integer | null

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#response-related-tag-id)

relatedTagID

integer | null

[​](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id#response-rank)

rank

integer | null

[Get tag by slug](https://docs.polymarket.com/api-reference/tags/get-tag-by-slug)
[Get related tags (relationships) by tag slug](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-slug)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.