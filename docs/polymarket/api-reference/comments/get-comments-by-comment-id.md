---
url: https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id
title: Get comments by comment id - Polymarket Documentation
scraped_at: 2025-11-03T15:03:37.188037
---

[Skip to main content](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Comments

Get comments by comment id

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get comments by comment id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/comments/{id}

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

{id}

Try it

Get comments by comment id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/comments/{id}

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

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#parameter-id)

id

integer

required

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#parameter-get-positions)

get\_positions

boolean

#### Response

200 - application/json

Comments

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-body)

body

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-parent-entity-type)

parentEntityType

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-parent-entity-id)

parentEntityID

integer | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-parent-comment-id)

parentCommentID

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-user-address)

userAddress

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-reply-address)

replyAddress

string | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-profile)

profile

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-reactions)

reactions

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-report-count)

reportCount

integer | null

[​](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id#response-reaction-count)

reactionCount

integer | null

[List comments](https://docs.polymarket.com/api-reference/comments/list-comments)
[Get comments by user address](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.