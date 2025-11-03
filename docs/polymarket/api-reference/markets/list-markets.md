---
url: https://docs.polymarket.com/api-reference/markets/list-markets
title: List markets - Polymarket Documentation
scraped_at: 2025-11-03T15:03:46.064049
---

[Skip to main content](https://docs.polymarket.com/api-reference/markets/list-markets#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Markets

List markets

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

List markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/markets

200

Copy

Ask AI

    [\
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
              {}\
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
    ]

GET

/

markets

Try it

List markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/markets

200

Copy

Ask AI

    [\
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
              {}\
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
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-order)

order

string

Comma-separated list of fields to order by

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-ascending)

ascending

boolean

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-id)

id

integer\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-slug)

slug

string\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-clob-token-ids)

clob\_token\_ids

string\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-condition-ids)

condition\_ids

string\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-market-maker-address)

market\_maker\_address

string\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-liquidity-num-min)

liquidity\_num\_min

number

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-liquidity-num-max)

liquidity\_num\_max

number

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-volume-num-min)

volume\_num\_min

number

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-volume-num-max)

volume\_num\_max

number

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-start-date-min)

start\_date\_min

string<date-time>

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-start-date-max)

start\_date\_max

string<date-time>

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-end-date-min)

end\_date\_min

string<date-time>

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-end-date-max)

end\_date\_max

string<date-time>

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-tag-id)

tag\_id

integer

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-related-tags)

related\_tags

boolean

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-cyom)

cyom

boolean

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-uma-resolution-status)

uma\_resolution\_status

string

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-game-id)

game\_id

string

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-sports-market-types)

sports\_market\_types

string\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-rewards-min-size)

rewards\_min\_size

number

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-question-ids)

question\_ids

string\[\]

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-include-tag)

include\_tag

boolean

[​](https://docs.polymarket.com/api-reference/markets/list-markets#parameter-closed)

closed

boolean

#### Response

200 - application/json

List of markets

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-question)

question

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-condition-id)

conditionId

string

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-twitter-card-image)

twitterCardImage

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-resolution-source)

resolutionSource

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-end-date)

endDate

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-category)

category

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-amm-type)

ammType

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-liquidity)

liquidity

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-sponsor-name)

sponsorName

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-sponsor-image)

sponsorImage

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-start-date)

startDate

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-x-axis-value)

xAxisValue

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-y-axis-value)

yAxisValue

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-denomination-token)

denominationToken

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-fee)

fee

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-image)

image

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-icon)

icon

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-lower-bound)

lowerBound

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-upper-bound)

upperBound

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-description)

description

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-outcomes)

outcomes

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-outcome-prices)

outcomePrices

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume)

volume

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-active)

active

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-market-type)

marketType

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-format-type)

formatType

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-lower-bound-date)

lowerBoundDate

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-upper-bound-date)

upperBoundDate

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-closed)

closed

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-market-maker-address)

marketMakerAddress

string

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-created-by)

createdBy

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-updated-by)

updatedBy

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-closed-time)

closedTime

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-wide-format)

wideFormat

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-new)

new

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-mailchimp-tag)

mailchimpTag

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-featured)

featured

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-archived)

archived

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-resolved-by)

resolvedBy

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-restricted)

restricted

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-market-group)

marketGroup

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-group-item-title)

groupItemTitle

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-group-item-threshold)

groupItemThreshold

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-question-id)

questionID

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-uma-end-date)

umaEndDate

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-enable-order-book)

enableOrderBook

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-order-price-min-tick-size)

orderPriceMinTickSize

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-order-min-size)

orderMinSize

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-uma-resolution-status)

umaResolutionStatus

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-curation-order)

curationOrder

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume-num)

volumeNum

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-liquidity-num)

liquidityNum

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-end-date-iso)

endDateIso

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-start-date-iso)

startDateIso

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-uma-end-date-iso)

umaEndDateIso

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-has-reviewed-dates)

hasReviewedDates

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-ready-for-cron)

readyForCron

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-comments-enabled)

commentsEnabled

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume24hr)

volume24hr

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1wk)

volume1wk

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1mo)

volume1mo

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1yr)

volume1yr

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-game-start-time)

gameStartTime

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-seconds-delay)

secondsDelay

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-clob-token-ids)

clobTokenIds

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-disqus-thread)

disqusThread

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-short-outcomes)

shortOutcomes

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-team-aid)

teamAID

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-team-bid)

teamBID

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-uma-bond)

umaBond

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-uma-reward)

umaReward

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-fpmm-live)

fpmmLive

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume24hr-amm)

volume24hrAmm

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1wk-amm)

volume1wkAmm

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1mo-amm)

volume1moAmm

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1yr-amm)

volume1yrAmm

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume24hr-clob)

volume24hrClob

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1wk-clob)

volume1wkClob

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1mo-clob)

volume1moClob

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume1yr-clob)

volume1yrClob

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume-amm)

volumeAmm

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-volume-clob)

volumeClob

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-liquidity-amm)

liquidityAmm

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-liquidity-clob)

liquidityClob

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-maker-base-fee)

makerBaseFee

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-taker-base-fee)

takerBaseFee

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-custom-liveness)

customLiveness

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-accepting-orders)

acceptingOrders

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-notifications-enabled)

notificationsEnabled

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-score)

score

integer | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-image-optimized)

imageOptimized

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-icon-optimized)

iconOptimized

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-events)

events

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-categories)

categories

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-tags)

tags

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-creator)

creator

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-ready)

ready

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-funded)

funded

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-past-slugs)

pastSlugs

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-ready-timestamp)

readyTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-funded-timestamp)

fundedTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-accepting-orders-timestamp)

acceptingOrdersTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-competitive)

competitive

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-rewards-min-size)

rewardsMinSize

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-rewards-max-spread)

rewardsMaxSpread

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-spread)

spread

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-automatically-resolved)

automaticallyResolved

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-one-day-price-change)

oneDayPriceChange

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-one-hour-price-change)

oneHourPriceChange

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-one-week-price-change)

oneWeekPriceChange

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-one-month-price-change)

oneMonthPriceChange

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-one-year-price-change)

oneYearPriceChange

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-last-trade-price)

lastTradePrice

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-best-bid)

bestBid

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-best-ask)

bestAsk

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-automatically-active)

automaticallyActive

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-clear-book-on-start)

clearBookOnStart

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-chart-color)

chartColor

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-series-color)

seriesColor

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-show-gmp-series)

showGmpSeries

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-show-gmp-outcome)

showGmpOutcome

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-manual-activation)

manualActivation

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-neg-risk-other)

negRiskOther

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-game-id)

gameId

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-group-item-range)

groupItemRange

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-sports-market-type)

sportsMarketType

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-line)

line

number | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-uma-resolution-statuses)

umaResolutionStatuses

string | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-pending-deployment)

pendingDeployment

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-deploying)

deploying

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-deploying-timestamp)

deployingTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-scheduled-deployment-timestamp)

scheduledDeploymentTimestamp

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-rfq-enabled)

rfqEnabled

boolean | null

[​](https://docs.polymarket.com/api-reference/markets/list-markets#response-event-start-time)

eventStartTime

string<date-time> | null

[Get event by slug](https://docs.polymarket.com/api-reference/events/get-event-by-slug)
[Get market by id](https://docs.polymarket.com/api-reference/markets/get-market-by-id)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.