---
url: https://docs.polymarket.com/api-reference/comments/list-comments
title: List comments - Polymarket Documentation
scraped_at: 2025-11-03T15:03:37.437744
---

[Skip to main content](https://docs.polymarket.com/api-reference/comments/list-comments#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Comments

List comments

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

List comments

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/comments

200

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "body": "<string>",\
        "parentEntityType": "<string>",\
        "parentEntityID": 123,\
        "parentCommentID": "<string>",\
        "userAddress": "<string>",\
        "replyAddress": "<string>",\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z",\
        "profile": {\
          "name": "<string>",\
          "pseudonym": "<string>",\
          "displayUsernamePublic": true,\
          "bio": "<string>",\
          "isMod": true,\
          "isCreator": true,\
          "proxyWallet": "<string>",\
          "baseAddress": "<string>",\
          "profileImage": "<string>",\
          "profileImageOptimized": {\
            "id": "<string>",\
            "imageUrlSource": "<string>",\
            "imageUrlOptimized": "<string>",\
            "imageSizeKbSource": 123,\
            "imageSizeKbOptimized": 123,\
            "imageOptimizedComplete": true,\
            "imageOptimizedLastUpdated": "<string>",\
            "relID": 123,\
            "field": "<string>",\
            "relname": "<string>"\
          },\
          "positions": [\
            {\
              "tokenId": "<string>",\
              "positionSize": "<string>"\
            }\
          ]\
        },\
        "reactions": [\
          {\
            "id": "<string>",\
            "commentID": 123,\
            "reactionType": "<string>",\
            "icon": "<string>",\
            "userAddress": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "profile": {\
              "name": "<string>",\
              "pseudonym": "<string>",\
              "displayUsernamePublic": true,\
              "bio": "<string>",\
              "isMod": true,\
              "isCreator": true,\
              "proxyWallet": "<string>",\
              "baseAddress": "<string>",\
              "profileImage": "<string>",\
              "profileImageOptimized": {\
                "id": "<string>",\
                "imageUrlSource": "<string>",\
                "imageUrlOptimized": "<string>",\
                "imageSizeKbSource": 123,\
                "imageSizeKbOptimized": 123,\
                "imageOptimizedComplete": true,\
                "imageOptimizedLastUpdated": "<string>",\
                "relID": 123,\
                "field": "<string>",\
                "relname": "<string>"\
              },\
              "positions": [\
                {\
                  "tokenId": "<string>",\
                  "positionSize": "<string>"\
                }\
              ]\
            }\
          }\
        ],\
        "reportCount": 123,\
        "reactionCount": 123\
      }\
    ]

GET

/

comments

Try it

List comments

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/comments

200

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "body": "<string>",\
        "parentEntityType": "<string>",\
        "parentEntityID": 123,\
        "parentCommentID": "<string>",\
        "userAddress": "<string>",\
        "replyAddress": "<string>",\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z",\
        "profile": {\
          "name": "<string>",\
          "pseudonym": "<string>",\
          "displayUsernamePublic": true,\
          "bio": "<string>",\
          "isMod": true,\
          "isCreator": true,\
          "proxyWallet": "<string>",\
          "baseAddress": "<string>",\
          "profileImage": "<string>",\
          "profileImageOptimized": {\
            "id": "<string>",\
            "imageUrlSource": "<string>",\
            "imageUrlOptimized": "<string>",\
            "imageSizeKbSource": 123,\
            "imageSizeKbOptimized": 123,\
            "imageOptimizedComplete": true,\
            "imageOptimizedLastUpdated": "<string>",\
            "relID": 123,\
            "field": "<string>",\
            "relname": "<string>"\
          },\
          "positions": [\
            {\
              "tokenId": "<string>",\
              "positionSize": "<string>"\
            }\
          ]\
        },\
        "reactions": [\
          {\
            "id": "<string>",\
            "commentID": 123,\
            "reactionType": "<string>",\
            "icon": "<string>",\
            "userAddress": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "profile": {\
              "name": "<string>",\
              "pseudonym": "<string>",\
              "displayUsernamePublic": true,\
              "bio": "<string>",\
              "isMod": true,\
              "isCreator": true,\
              "proxyWallet": "<string>",\
              "baseAddress": "<string>",\
              "profileImage": "<string>",\
              "profileImageOptimized": {\
                "id": "<string>",\
                "imageUrlSource": "<string>",\
                "imageUrlOptimized": "<string>",\
                "imageSizeKbSource": 123,\
                "imageSizeKbOptimized": 123,\
                "imageOptimizedComplete": true,\
                "imageOptimizedLastUpdated": "<string>",\
                "relID": 123,\
                "field": "<string>",\
                "relname": "<string>"\
              },\
              "positions": [\
                {\
                  "tokenId": "<string>",\
                  "positionSize": "<string>"\
                }\
              ]\
            }\
          }\
        ],\
        "reportCount": 123,\
        "reactionCount": 123\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-order)

order

string

Comma-separated list of fields to order by

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-ascending)

ascending

boolean

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-parent-entity-type)

parent\_entity\_type

enum<string>

Available options:

`Event`,

`Series`,

`market`

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-parent-entity-id)

parent\_entity\_id

integer

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-get-positions)

get\_positions

boolean

[​](https://docs.polymarket.com/api-reference/comments/list-comments#parameter-holders-only)

holders\_only

boolean

#### Response

200 - application/json

List of comments

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-body)

body

string | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-parent-entity-type)

parentEntityType

string | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-parent-entity-id)

parentEntityID

integer | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-parent-comment-id)

parentCommentID

string | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-user-address)

userAddress

string | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-reply-address)

replyAddress

string | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-profile)

profile

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-reactions)

reactions

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-report-count)

reportCount

integer | null

[​](https://docs.polymarket.com/api-reference/comments/list-comments#response-reaction-count)

reactionCount

integer | null

[Get series by id](https://docs.polymarket.com/api-reference/series/get-series-by-id)
[Get comments by comment id](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.