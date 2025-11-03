---
url: https://docs.polymarket.com/api-reference/series/get-series-by-id
title: Get series by id - Polymarket Documentation
scraped_at: 2025-11-03T15:03:51.339634
---

[Skip to main content](https://docs.polymarket.com/api-reference/series/get-series-by-id#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Series

Get series by id

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get series by id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/series/{id}

200

404

Copy

Ask AI

    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "seriesType": "<string>",
      "recurrence": "<string>",
      "description": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": true,
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": "<string>",
      "volume24hr": 123,
      "volume": 123,
      "liquidity": 123,
      "startDate": "2023-11-07T05:31:56Z",
      "pythTokenID": "<string>",
      "cgAssetName": "<string>",
      "score": 123,
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
      ],
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
      ],
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
      ],
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
      ],
      "commentCount": 123,
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
      ]
    }

GET

/

series

/

{id}

Try it

Get series by id

cURL

Copy

Ask AI

    curl --request GET \
      --url https://gamma-api.polymarket.com/series/{id}

200

404

Copy

Ask AI

    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "seriesType": "<string>",
      "recurrence": "<string>",
      "description": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": true,
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": "<string>",
      "volume24hr": 123,
      "volume": 123,
      "liquidity": 123,
      "startDate": "2023-11-07T05:31:56Z",
      "pythTokenID": "<string>",
      "cgAssetName": "<string>",
      "score": 123,
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
      ],
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
      ],
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
      ],
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
      ],
      "commentCount": 123,
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
      ]
    }

#### Path Parameters

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#parameter-id)

id

integer

required

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#parameter-include-chat)

include\_chat

boolean

#### Response

200

application/json

Series

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-id)

id

string

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-ticker)

ticker

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-slug)

slug

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-title)

title

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-subtitle)

subtitle

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-series-type)

seriesType

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-recurrence)

recurrence

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-description)

description

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-image)

image

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-icon)

icon

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-layout)

layout

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-active)

active

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-closed)

closed

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-archived)

archived

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-new)

new

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-featured)

featured

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-restricted)

restricted

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-is-template)

isTemplate

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-template-variables)

templateVariables

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-published-at)

publishedAt

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-created-by)

createdBy

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-updated-by)

updatedBy

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-created-at)

createdAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-updated-at)

updatedAt

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-comments-enabled)

commentsEnabled

boolean | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-competitive)

competitive

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-volume24hr)

volume24hr

number | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-volume)

volume

number | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-liquidity)

liquidity

number | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-start-date)

startDate

string<date-time> | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-pyth-token-id)

pythTokenID

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-cg-asset-name)

cgAssetName

string | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-score)

score

integer | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-events)

events

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-collections)

collections

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-categories)

categories

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-tags)

tags

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-comment-count)

commentCount

integer | null

[​](https://docs.polymarket.com/api-reference/series/get-series-by-id#response-chats)

chats

object\[\]

Show child attributes

[List series](https://docs.polymarket.com/api-reference/series/list-series)
[List comments](https://docs.polymarket.com/api-reference/comments/list-comments)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.