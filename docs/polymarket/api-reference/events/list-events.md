---
url: https://docs.polymarket.com/api-reference/events/list-events
title: List events - Polymarket Documentation
scraped_at: 2025-11-03T15:03:42.243588
---

[Skip to main content](https://docs.polymarket.com/api-reference/events/list-events#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

⌘K

Search...

Navigation

Events

List events

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

List events

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/events

200

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "ticker": "<string>",\
        "slug": "<string>",\
        "title": "<string>",\
        "subtitle": "<string>",\
        "description": "<string>",\
        "resolutionSource": "<string>",\
        "startDate": "2023-11-07T05:31:56Z",\
        "creationDate": "2023-11-07T05:31:56Z",\
        "endDate": "2023-11-07T05:31:56Z",\
        "image": "<string>",\
        "icon": "<string>",\
        "active": true,\
        "closed": true,\
        "archived": true,\
        "new": true,\
        "featured": true,\
        "restricted": true,\
        "liquidity": 123,\
        "volume": 123,\
        "openInterest": 123,\
        "sortBy": "<string>",\
        "category": "<string>",\
        "subcategory": "<string>",\
        "isTemplate": true,\
        "templateVariables": "<string>",\
        "published_at": "<string>",\
        "createdBy": "<string>",\
        "updatedBy": "<string>",\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z",\
        "commentsEnabled": true,\
        "competitive": 123,\
        "volume24hr": 123,\
        "volume1wk": 123,\
        "volume1mo": 123,\
        "volume1yr": 123,\
        "featuredImage": "<string>",\
        "disqusThread": "<string>",\
        "parentEvent": "<string>",\
        "enableOrderBook": true,\
        "liquidityAmm": 123,\
        "liquidityClob": 123,\
        "negRisk": true,\
        "negRiskMarketID": "<string>",\
        "negRiskFeeBips": 123,\
        "commentCount": 123,\
        "imageOptimized": {\
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
        "iconOptimized": {\
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
        "featuredImageOptimized": {\
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
        "subEvents": [\
          "<string>"\
        ],\
        "markets": [\
          {\
            "id": "<string>",\
            "question": "<string>",\
            "conditionId": "<string>",\
            "slug": "<string>",\
            "twitterCardImage": "<string>",\
            "resolutionSource": "<string>",\
            "endDate": "2023-11-07T05:31:56Z",\
            "category": "<string>",\
            "ammType": "<string>",\
            "liquidity": "<string>",\
            "sponsorName": "<string>",\
            "sponsorImage": "<string>",\
            "startDate": "2023-11-07T05:31:56Z",\
            "xAxisValue": "<string>",\
            "yAxisValue": "<string>",\
            "denominationToken": "<string>",\
            "fee": "<string>",\
            "image": "<string>",\
            "icon": "<string>",\
            "lowerBound": "<string>",\
            "upperBound": "<string>",\
            "description": "<string>",\
            "outcomes": "<string>",\
            "outcomePrices": "<string>",\
            "volume": "<string>",\
            "active": true,\
            "marketType": "<string>",\
            "formatType": "<string>",\
            "lowerBoundDate": "<string>",\
            "upperBoundDate": "<string>",\
            "closed": true,\
            "marketMakerAddress": "<string>",\
            "createdBy": 123,\
            "updatedBy": 123,\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z",\
            "closedTime": "<string>",\
            "wideFormat": true,\
            "new": true,\
            "mailchimpTag": "<string>",\
            "featured": true,\
            "archived": true,\
            "resolvedBy": "<string>",\
            "restricted": true,\
            "marketGroup": 123,\
            "groupItemTitle": "<string>",\
            "groupItemThreshold": "<string>",\
            "questionID": "<string>",\
            "umaEndDate": "<string>",\
            "enableOrderBook": true,\
            "orderPriceMinTickSize": 123,\
            "orderMinSize": 123,\
            "umaResolutionStatus": "<string>",\
            "curationOrder": 123,\
            "volumeNum": 123,\
            "liquidityNum": 123,\
            "endDateIso": "<string>",\
            "startDateIso": "<string>",\
            "umaEndDateIso": "<string>",\
            "hasReviewedDates": true,\
            "readyForCron": true,\
            "commentsEnabled": true,\
            "volume24hr": 123,\
            "volume1wk": 123,\
            "volume1mo": 123,\
            "volume1yr": 123,\
            "gameStartTime": "<string>",\
            "secondsDelay": 123,\
            "clobTokenIds": "<string>",\
            "disqusThread": "<string>",\
            "shortOutcomes": "<string>",\
            "teamAID": "<string>",\
            "teamBID": "<string>",\
            "umaBond": "<string>",\
            "umaReward": "<string>",\
            "fpmmLive": true,\
            "volume24hrAmm": 123,\
            "volume1wkAmm": 123,\
            "volume1moAmm": 123,\
            "volume1yrAmm": 123,\
            "volume24hrClob": 123,\
            "volume1wkClob": 123,\
            "volume1moClob": 123,\
            "volume1yrClob": 123,\
            "volumeAmm": 123,\
            "volumeClob": 123,\
            "liquidityAmm": 123,\
            "liquidityClob": 123,\
            "makerBaseFee": 123,\
            "takerBaseFee": 123,\
            "customLiveness": 123,\
            "acceptingOrders": true,\
            "notificationsEnabled": true,\
            "score": 123,\
            "imageOptimized": {\
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
            "iconOptimized": {\
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
            "events": [\
              {}\
            ],\
            "categories": [\
              {\
                "id": "<string>",\
                "label": "<string>",\
                "parentCategory": "<string>",\
                "slug": "<string>",\
                "publishedAt": "<string>",\
                "createdBy": "<string>",\
                "updatedBy": "<string>",\
                "createdAt": "2023-11-07T05:31:56Z",\
                "updatedAt": "2023-11-07T05:31:56Z"\
              }\
            ],\
            "tags": [\
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
            ],\
            "creator": "<string>",\
            "ready": true,\
            "funded": true,\
            "pastSlugs": "<string>",\
            "readyTimestamp": "2023-11-07T05:31:56Z",\
            "fundedTimestamp": "2023-11-07T05:31:56Z",\
            "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",\
            "competitive": 123,\
            "rewardsMinSize": 123,\
            "rewardsMaxSpread": 123,\
            "spread": 123,\
            "automaticallyResolved": true,\
            "oneDayPriceChange": 123,\
            "oneHourPriceChange": 123,\
            "oneWeekPriceChange": 123,\
            "oneMonthPriceChange": 123,\
            "oneYearPriceChange": 123,\
            "lastTradePrice": 123,\
            "bestBid": 123,\
            "bestAsk": 123,\
            "automaticallyActive": true,\
            "clearBookOnStart": true,\
            "chartColor": "<string>",\
            "seriesColor": "<string>",\
            "showGmpSeries": true,\
            "showGmpOutcome": true,\
            "manualActivation": true,\
            "negRiskOther": true,\
            "gameId": "<string>",\
            "groupItemRange": "<string>",\
            "sportsMarketType": "<string>",\
            "line": 123,\
            "umaResolutionStatuses": "<string>",\
            "pendingDeployment": true,\
            "deploying": true,\
            "deployingTimestamp": "2023-11-07T05:31:56Z",\
            "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",\
            "rfqEnabled": true,\
            "eventStartTime": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "series": [\
          {\
            "id": "<string>",\
            "ticker": "<string>",\
            "slug": "<string>",\
            "title": "<string>",\
            "subtitle": "<string>",\
            "seriesType": "<string>",\
            "recurrence": "<string>",\
            "description": "<string>",\
            "image": "<string>",\
            "icon": "<string>",\
            "layout": "<string>",\
            "active": true,\
            "closed": true,\
            "archived": true,\
            "new": true,\
            "featured": true,\
            "restricted": true,\
            "isTemplate": true,\
            "templateVariables": true,\
            "publishedAt": "<string>",\
            "createdBy": "<string>",\
            "updatedBy": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z",\
            "commentsEnabled": true,\
            "competitive": "<string>",\
            "volume24hr": 123,\
            "volume": 123,\
            "liquidity": 123,\
            "startDate": "2023-11-07T05:31:56Z",\
            "pythTokenID": "<string>",\
            "cgAssetName": "<string>",\
            "score": 123,\
            "events": [\
              {}\
            ],\
            "collections": [\
              {\
                "id": "<string>",\
                "ticker": "<string>",\
                "slug": "<string>",\
                "title": "<string>",\
                "subtitle": "<string>",\
                "collectionType": "<string>",\
                "description": "<string>",\
                "tags": "<string>",\
                "image": "<string>",\
                "icon": "<string>",\
                "headerImage": "<string>",\
                "layout": "<string>",\
                "active": true,\
                "closed": true,\
                "archived": true,\
                "new": true,\
                "featured": true,\
                "restricted": true,\
                "isTemplate": true,\
                "templateVariables": "<string>",\
                "publishedAt": "<string>",\
                "createdBy": "<string>",\
                "updatedBy": "<string>",\
                "createdAt": "2023-11-07T05:31:56Z",\
                "updatedAt": "2023-11-07T05:31:56Z",\
                "commentsEnabled": true,\
                "imageOptimized": {\
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
                "iconOptimized": {\
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
                "headerImageOptimized": {\
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
                }\
              }\
            ],\
            "categories": [\
              {\
                "id": "<string>",\
                "label": "<string>",\
                "parentCategory": "<string>",\
                "slug": "<string>",\
                "publishedAt": "<string>",\
                "createdBy": "<string>",\
                "updatedBy": "<string>",\
                "createdAt": "2023-11-07T05:31:56Z",\
                "updatedAt": "2023-11-07T05:31:56Z"\
              }\
            ],\
            "tags": [\
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
            ],\
            "commentCount": 123,\
            "chats": [\
              {\
                "id": "<string>",\
                "channelId": "<string>",\
                "channelName": "<string>",\
                "channelImage": "<string>",\
                "live": true,\
                "startTime": "2023-11-07T05:31:56Z",\
                "endTime": "2023-11-07T05:31:56Z"\
              }\
            ]\
          }\
        ],\
        "categories": [\
          {\
            "id": "<string>",\
            "label": "<string>",\
            "parentCategory": "<string>",\
            "slug": "<string>",\
            "publishedAt": "<string>",\
            "createdBy": "<string>",\
            "updatedBy": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "collections": [\
          {\
            "id": "<string>",\
            "ticker": "<string>",\
            "slug": "<string>",\
            "title": "<string>",\
            "subtitle": "<string>",\
            "collectionType": "<string>",\
            "description": "<string>",\
            "tags": "<string>",\
            "image": "<string>",\
            "icon": "<string>",\
            "headerImage": "<string>",\
            "layout": "<string>",\
            "active": true,\
            "closed": true,\
            "archived": true,\
            "new": true,\
            "featured": true,\
            "restricted": true,\
            "isTemplate": true,\
            "templateVariables": "<string>",\
            "publishedAt": "<string>",\
            "createdBy": "<string>",\
            "updatedBy": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z",\
            "commentsEnabled": true,\
            "imageOptimized": {\
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
            "iconOptimized": {\
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
            "headerImageOptimized": {\
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
            }\
          }\
        ],\
        "tags": [\
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
        ],\
        "cyom": true,\
        "closedTime": "2023-11-07T05:31:56Z",\
        "showAllOutcomes": true,\
        "showMarketImages": true,\
        "automaticallyResolved": true,\
        "enableNegRisk": true,\
        "automaticallyActive": true,\
        "eventDate": "<string>",\
        "startTime": "2023-11-07T05:31:56Z",\
        "eventWeek": 123,\
        "seriesSlug": "<string>",\
        "score": "<string>",\
        "elapsed": "<string>",\
        "period": "<string>",\
        "live": true,\
        "ended": true,\
        "finishedTimestamp": "2023-11-07T05:31:56Z",\
        "gmpChartMode": "<string>",\
        "eventCreators": [\
          {\
            "id": "<string>",\
            "creatorName": "<string>",\
            "creatorHandle": "<string>",\
            "creatorUrl": "<string>",\
            "creatorImage": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "tweetCount": 123,\
        "chats": [\
          {\
            "id": "<string>",\
            "channelId": "<string>",\
            "channelName": "<string>",\
            "channelImage": "<string>",\
            "live": true,\
            "startTime": "2023-11-07T05:31:56Z",\
            "endTime": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "featuredOrder": 123,\
        "estimateValue": true,\
        "cantEstimate": true,\
        "estimatedValue": "<string>",\
        "templates": [\
          {\
            "id": "<string>",\
            "eventTitle": "<string>",\
            "eventSlug": "<string>",\
            "eventImage": "<string>",\
            "marketTitle": "<string>",\
            "description": "<string>",\
            "resolutionSource": "<string>",\
            "negRisk": true,\
            "sortBy": "<string>",\
            "showMarketImages": true,\
            "seriesSlug": "<string>",\
            "outcomes": "<string>"\
          }\
        ],\
        "spreadsMainLine": 123,\
        "totalsMainLine": 123,\
        "carouselMap": "<string>",\
        "pendingDeployment": true,\
        "deploying": true,\
        "deployingTimestamp": "2023-11-07T05:31:56Z",\
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",\
        "gameStatus": "<string>"\
      }\
    ]

GET

/

events

Try it

List events

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/events

200

Copy

Ask AI

    [\
      {\
        "id": "<string>",\
        "ticker": "<string>",\
        "slug": "<string>",\
        "title": "<string>",\
        "subtitle": "<string>",\
        "description": "<string>",\
        "resolutionSource": "<string>",\
        "startDate": "2023-11-07T05:31:56Z",\
        "creationDate": "2023-11-07T05:31:56Z",\
        "endDate": "2023-11-07T05:31:56Z",\
        "image": "<string>",\
        "icon": "<string>",\
        "active": true,\
        "closed": true,\
        "archived": true,\
        "new": true,\
        "featured": true,\
        "restricted": true,\
        "liquidity": 123,\
        "volume": 123,\
        "openInterest": 123,\
        "sortBy": "<string>",\
        "category": "<string>",\
        "subcategory": "<string>",\
        "isTemplate": true,\
        "templateVariables": "<string>",\
        "published_at": "<string>",\
        "createdBy": "<string>",\
        "updatedBy": "<string>",\
        "createdAt": "2023-11-07T05:31:56Z",\
        "updatedAt": "2023-11-07T05:31:56Z",\
        "commentsEnabled": true,\
        "competitive": 123,\
        "volume24hr": 123,\
        "volume1wk": 123,\
        "volume1mo": 123,\
        "volume1yr": 123,\
        "featuredImage": "<string>",\
        "disqusThread": "<string>",\
        "parentEvent": "<string>",\
        "enableOrderBook": true,\
        "liquidityAmm": 123,\
        "liquidityClob": 123,\
        "negRisk": true,\
        "negRiskMarketID": "<string>",\
        "negRiskFeeBips": 123,\
        "commentCount": 123,\
        "imageOptimized": {\
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
        "iconOptimized": {\
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
        "featuredImageOptimized": {\
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
        "subEvents": [\
          "<string>"\
        ],\
        "markets": [\
          {\
            "id": "<string>",\
            "question": "<string>",\
            "conditionId": "<string>",\
            "slug": "<string>",\
            "twitterCardImage": "<string>",\
            "resolutionSource": "<string>",\
            "endDate": "2023-11-07T05:31:56Z",\
            "category": "<string>",\
            "ammType": "<string>",\
            "liquidity": "<string>",\
            "sponsorName": "<string>",\
            "sponsorImage": "<string>",\
            "startDate": "2023-11-07T05:31:56Z",\
            "xAxisValue": "<string>",\
            "yAxisValue": "<string>",\
            "denominationToken": "<string>",\
            "fee": "<string>",\
            "image": "<string>",\
            "icon": "<string>",\
            "lowerBound": "<string>",\
            "upperBound": "<string>",\
            "description": "<string>",\
            "outcomes": "<string>",\
            "outcomePrices": "<string>",\
            "volume": "<string>",\
            "active": true,\
            "marketType": "<string>",\
            "formatType": "<string>",\
            "lowerBoundDate": "<string>",\
            "upperBoundDate": "<string>",\
            "closed": true,\
            "marketMakerAddress": "<string>",\
            "createdBy": 123,\
            "updatedBy": 123,\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z",\
            "closedTime": "<string>",\
            "wideFormat": true,\
            "new": true,\
            "mailchimpTag": "<string>",\
            "featured": true,\
            "archived": true,\
            "resolvedBy": "<string>",\
            "restricted": true,\
            "marketGroup": 123,\
            "groupItemTitle": "<string>",\
            "groupItemThreshold": "<string>",\
            "questionID": "<string>",\
            "umaEndDate": "<string>",\
            "enableOrderBook": true,\
            "orderPriceMinTickSize": 123,\
            "orderMinSize": 123,\
            "umaResolutionStatus": "<string>",\
            "curationOrder": 123,\
            "volumeNum": 123,\
            "liquidityNum": 123,\
            "endDateIso": "<string>",\
            "startDateIso": "<string>",\
            "umaEndDateIso": "<string>",\
            "hasReviewedDates": true,\
            "readyForCron": true,\
            "commentsEnabled": true,\
            "volume24hr": 123,\
            "volume1wk": 123,\
            "volume1mo": 123,\
            "volume1yr": 123,\
            "gameStartTime": "<string>",\
            "secondsDelay": 123,\
            "clobTokenIds": "<string>",\
            "disqusThread": "<string>",\
            "shortOutcomes": "<string>",\
            "teamAID": "<string>",\
            "teamBID": "<string>",\
            "umaBond": "<string>",\
            "umaReward": "<string>",\
            "fpmmLive": true,\
            "volume24hrAmm": 123,\
            "volume1wkAmm": 123,\
            "volume1moAmm": 123,\
            "volume1yrAmm": 123,\
            "volume24hrClob": 123,\
            "volume1wkClob": 123,\
            "volume1moClob": 123,\
            "volume1yrClob": 123,\
            "volumeAmm": 123,\
            "volumeClob": 123,\
            "liquidityAmm": 123,\
            "liquidityClob": 123,\
            "makerBaseFee": 123,\
            "takerBaseFee": 123,\
            "customLiveness": 123,\
            "acceptingOrders": true,\
            "notificationsEnabled": true,\
            "score": 123,\
            "imageOptimized": {\
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
            "iconOptimized": {\
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
            "events": [\
              {}\
            ],\
            "categories": [\
              {\
                "id": "<string>",\
                "label": "<string>",\
                "parentCategory": "<string>",\
                "slug": "<string>",\
                "publishedAt": "<string>",\
                "createdBy": "<string>",\
                "updatedBy": "<string>",\
                "createdAt": "2023-11-07T05:31:56Z",\
                "updatedAt": "2023-11-07T05:31:56Z"\
              }\
            ],\
            "tags": [\
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
            ],\
            "creator": "<string>",\
            "ready": true,\
            "funded": true,\
            "pastSlugs": "<string>",\
            "readyTimestamp": "2023-11-07T05:31:56Z",\
            "fundedTimestamp": "2023-11-07T05:31:56Z",\
            "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",\
            "competitive": 123,\
            "rewardsMinSize": 123,\
            "rewardsMaxSpread": 123,\
            "spread": 123,\
            "automaticallyResolved": true,\
            "oneDayPriceChange": 123,\
            "oneHourPriceChange": 123,\
            "oneWeekPriceChange": 123,\
            "oneMonthPriceChange": 123,\
            "oneYearPriceChange": 123,\
            "lastTradePrice": 123,\
            "bestBid": 123,\
            "bestAsk": 123,\
            "automaticallyActive": true,\
            "clearBookOnStart": true,\
            "chartColor": "<string>",\
            "seriesColor": "<string>",\
            "showGmpSeries": true,\
            "showGmpOutcome": true,\
            "manualActivation": true,\
            "negRiskOther": true,\
            "gameId": "<string>",\
            "groupItemRange": "<string>",\
            "sportsMarketType": "<string>",\
            "line": 123,\
            "umaResolutionStatuses": "<string>",\
            "pendingDeployment": true,\
            "deploying": true,\
            "deployingTimestamp": "2023-11-07T05:31:56Z",\
            "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",\
            "rfqEnabled": true,\
            "eventStartTime": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "series": [\
          {\
            "id": "<string>",\
            "ticker": "<string>",\
            "slug": "<string>",\
            "title": "<string>",\
            "subtitle": "<string>",\
            "seriesType": "<string>",\
            "recurrence": "<string>",\
            "description": "<string>",\
            "image": "<string>",\
            "icon": "<string>",\
            "layout": "<string>",\
            "active": true,\
            "closed": true,\
            "archived": true,\
            "new": true,\
            "featured": true,\
            "restricted": true,\
            "isTemplate": true,\
            "templateVariables": true,\
            "publishedAt": "<string>",\
            "createdBy": "<string>",\
            "updatedBy": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z",\
            "commentsEnabled": true,\
            "competitive": "<string>",\
            "volume24hr": 123,\
            "volume": 123,\
            "liquidity": 123,\
            "startDate": "2023-11-07T05:31:56Z",\
            "pythTokenID": "<string>",\
            "cgAssetName": "<string>",\
            "score": 123,\
            "events": [\
              {}\
            ],\
            "collections": [\
              {\
                "id": "<string>",\
                "ticker": "<string>",\
                "slug": "<string>",\
                "title": "<string>",\
                "subtitle": "<string>",\
                "collectionType": "<string>",\
                "description": "<string>",\
                "tags": "<string>",\
                "image": "<string>",\
                "icon": "<string>",\
                "headerImage": "<string>",\
                "layout": "<string>",\
                "active": true,\
                "closed": true,\
                "archived": true,\
                "new": true,\
                "featured": true,\
                "restricted": true,\
                "isTemplate": true,\
                "templateVariables": "<string>",\
                "publishedAt": "<string>",\
                "createdBy": "<string>",\
                "updatedBy": "<string>",\
                "createdAt": "2023-11-07T05:31:56Z",\
                "updatedAt": "2023-11-07T05:31:56Z",\
                "commentsEnabled": true,\
                "imageOptimized": {\
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
                "iconOptimized": {\
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
                "headerImageOptimized": {\
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
                }\
              }\
            ],\
            "categories": [\
              {\
                "id": "<string>",\
                "label": "<string>",\
                "parentCategory": "<string>",\
                "slug": "<string>",\
                "publishedAt": "<string>",\
                "createdBy": "<string>",\
                "updatedBy": "<string>",\
                "createdAt": "2023-11-07T05:31:56Z",\
                "updatedAt": "2023-11-07T05:31:56Z"\
              }\
            ],\
            "tags": [\
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
            ],\
            "commentCount": 123,\
            "chats": [\
              {\
                "id": "<string>",\
                "channelId": "<string>",\
                "channelName": "<string>",\
                "channelImage": "<string>",\
                "live": true,\
                "startTime": "2023-11-07T05:31:56Z",\
                "endTime": "2023-11-07T05:31:56Z"\
              }\
            ]\
          }\
        ],\
        "categories": [\
          {\
            "id": "<string>",\
            "label": "<string>",\
            "parentCategory": "<string>",\
            "slug": "<string>",\
            "publishedAt": "<string>",\
            "createdBy": "<string>",\
            "updatedBy": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "collections": [\
          {\
            "id": "<string>",\
            "ticker": "<string>",\
            "slug": "<string>",\
            "title": "<string>",\
            "subtitle": "<string>",\
            "collectionType": "<string>",\
            "description": "<string>",\
            "tags": "<string>",\
            "image": "<string>",\
            "icon": "<string>",\
            "headerImage": "<string>",\
            "layout": "<string>",\
            "active": true,\
            "closed": true,\
            "archived": true,\
            "new": true,\
            "featured": true,\
            "restricted": true,\
            "isTemplate": true,\
            "templateVariables": "<string>",\
            "publishedAt": "<string>",\
            "createdBy": "<string>",\
            "updatedBy": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z",\
            "commentsEnabled": true,\
            "imageOptimized": {\
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
            "iconOptimized": {\
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
            "headerImageOptimized": {\
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
            }\
          }\
        ],\
        "tags": [\
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
        ],\
        "cyom": true,\
        "closedTime": "2023-11-07T05:31:56Z",\
        "showAllOutcomes": true,\
        "showMarketImages": true,\
        "automaticallyResolved": true,\
        "enableNegRisk": true,\
        "automaticallyActive": true,\
        "eventDate": "<string>",\
        "startTime": "2023-11-07T05:31:56Z",\
        "eventWeek": 123,\
        "seriesSlug": "<string>",\
        "score": "<string>",\
        "elapsed": "<string>",\
        "period": "<string>",\
        "live": true,\
        "ended": true,\
        "finishedTimestamp": "2023-11-07T05:31:56Z",\
        "gmpChartMode": "<string>",\
        "eventCreators": [\
          {\
            "id": "<string>",\
            "creatorName": "<string>",\
            "creatorHandle": "<string>",\
            "creatorUrl": "<string>",\
            "creatorImage": "<string>",\
            "createdAt": "2023-11-07T05:31:56Z",\
            "updatedAt": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "tweetCount": 123,\
        "chats": [\
          {\
            "id": "<string>",\
            "channelId": "<string>",\
            "channelName": "<string>",\
            "channelImage": "<string>",\
            "live": true,\
            "startTime": "2023-11-07T05:31:56Z",\
            "endTime": "2023-11-07T05:31:56Z"\
          }\
        ],\
        "featuredOrder": 123,\
        "estimateValue": true,\
        "cantEstimate": true,\
        "estimatedValue": "<string>",\
        "templates": [\
          {\
            "id": "<string>",\
            "eventTitle": "<string>",\
            "eventSlug": "<string>",\
            "eventImage": "<string>",\
            "marketTitle": "<string>",\
            "description": "<string>",\
            "resolutionSource": "<string>",\
            "negRisk": true,\
            "sortBy": "<string>",\
            "showMarketImages": true,\
            "seriesSlug": "<string>",\
            "outcomes": "<string>"\
          }\
        ],\
        "spreadsMainLine": 123,\
        "totalsMainLine": 123,\
        "carouselMap": "<string>",\
        "pendingDeployment": true,\
        "deploying": true,\
        "deployingTimestamp": "2023-11-07T05:31:56Z",\
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",\
        "gameStatus": "<string>"\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-order)

order

string

Comma-separated list of fields to order by

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-ascending)

ascending

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-id)

id

integer\[\]

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-slug)

slug

string\[\]

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-tag-id)

tag\_id

integer

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-exclude-tag-id)

exclude\_tag\_id

integer\[\]

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-related-tags)

related\_tags

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-featured)

featured

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-cyom)

cyom

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-include-chat)

include\_chat

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-include-template)

include\_template

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-recurrence)

recurrence

string

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-closed)

closed

boolean

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-start-date-min)

start\_date\_min

string<date-time>

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-start-date-max)

start\_date\_max

string<date-time>

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-end-date-min)

end\_date\_min

string<date-time>

[​](https://docs.polymarket.com/api-reference/events/list-events#parameter-end-date-max)

end\_date\_max

string<date-time>

#### Response

200 - application/json

List of events

[​](https://docs.polymarket.com/api-reference/events/list-events#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/events/list-events#response-ticker)

ticker

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-title)

title

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-subtitle)

subtitle

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-description)

description

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-resolution-source)

resolutionSource

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-start-date)

startDate

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-creation-date)

creationDate

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-end-date)

endDate

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-image)

image

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-icon)

icon

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-active)

active

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-closed)

closed

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-archived)

archived

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-new)

new

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-featured)

featured

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-restricted)

restricted

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-liquidity)

liquidity

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-volume)

volume

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-open-interest)

openInterest

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-sort-by)

sortBy

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-category)

category

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-subcategory)

subcategory

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-is-template)

isTemplate

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-template-variables)

templateVariables

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-published-at)

published\_at

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-created-by)

createdBy

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-updated-by)

updatedBy

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-comments-enabled)

commentsEnabled

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-competitive)

competitive

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-volume24hr)

volume24hr

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-volume1wk)

volume1wk

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-volume1mo)

volume1mo

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-volume1yr)

volume1yr

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-featured-image)

featuredImage

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-disqus-thread)

disqusThread

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-parent-event)

parentEvent

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-enable-order-book)

enableOrderBook

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-liquidity-amm)

liquidityAmm

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-liquidity-clob)

liquidityClob

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-neg-risk)

negRisk

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-neg-risk-market-id)

negRiskMarketID

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-neg-risk-fee-bips)

negRiskFeeBips

integer | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-comment-count)

commentCount

integer | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-image-optimized)

imageOptimized

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-icon-optimized)

iconOptimized

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-featured-image-optimized)

featuredImageOptimized

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-sub-events)

subEvents

string\[\] | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-markets)

markets

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-series)

series

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-categories)

categories

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-collections)

collections

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-tags)

tags

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-cyom)

cyom

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-closed-time)

closedTime

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-show-all-outcomes)

showAllOutcomes

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-show-market-images)

showMarketImages

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-automatically-resolved)

automaticallyResolved

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-enable-neg-risk)

enableNegRisk

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-automatically-active)

automaticallyActive

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-event-date)

eventDate

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-start-time)

startTime

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-event-week)

eventWeek

integer | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-series-slug)

seriesSlug

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-score)

score

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-elapsed)

elapsed

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-period)

period

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-live)

live

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-ended)

ended

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-finished-timestamp)

finishedTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-gmp-chart-mode)

gmpChartMode

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-event-creators)

eventCreators

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-tweet-count)

tweetCount

integer | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-chats)

chats

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-featured-order)

featuredOrder

integer | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-estimate-value)

estimateValue

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-cant-estimate)

cantEstimate

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-estimated-value)

estimatedValue

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-templates)

templates

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/events/list-events#response-spreads-main-line)

spreadsMainLine

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-totals-main-line)

totalsMainLine

number | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-carousel-map)

carouselMap

string | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-pending-deployment)

pendingDeployment

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-deploying)

deploying

boolean | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-deploying-timestamp)

deployingTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-scheduled-deployment-timestamp)

scheduledDeploymentTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/events/list-events#response-game-status)

gameStatus

string | null

[Get tags related to a tag slug](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug)
[Get event by id](https://docs.polymarket.com/api-reference/events/get-event-by-id)

⌘I