---
url: https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address
title: Get comments by user address - Polymarket Documentation
scraped_at: 2025-11-03T15:03:37.438426
---

[Skip to main content](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Comments

Get comments by user address

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get comments by user address

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/comments/user_address/{user_address}

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

/

user\_address

/

{user\_address}

Try it

Get comments by user address

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/comments/user_address/{user_address}

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

#### Path Parameters

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#parameter-user-address)

user\_address

string

required

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#parameter-order)

order

string

Comma-separated list of fields to order by

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#parameter-ascending)

ascending

boolean

#### Response

200 - application/json

Comments

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-body)

body

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-parent-entity-type)

parentEntityType

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-parent-entity-id)

parentEntityID

integer | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-parent-comment-id)

parentCommentID

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-user-address)

userAddress

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-reply-address)

replyAddress

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-profile)

profile

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-reactions)

reactions

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-report-count)

reportCount

integer | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address#response-reaction-count)

reactionCount

integer | null

[Get comments by comment id](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id)
[Search markets, events, and profiles](https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.