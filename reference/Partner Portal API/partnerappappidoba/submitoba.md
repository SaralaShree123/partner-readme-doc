---
title: Submit OBA request for an app
excerpt: This is an app level API to submit request for OBA status.
api:
  file: SubmitOBAVer1.json
  operationId: submitOba
hidden: true
---
# Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/oba' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
  "additional_supporting_information": "We are also featured in Planet Succulent and Prickly Digest",
  "business_website_url": "https://www.luckyshrub.com",
  "parent_business_or_brand": "Lucky Shrub LLC",
  "primary_country_of_operation": "United States of America",
  "primary_language": "English",
  "supporting_links": [
    "https://www.retailreview.com/gardening/2025/lucky-shrub",
    "https://www.faster-company.com/2025/online-nursies-are-making-green-waves",
    "https://www.succulentscene.com/2025/new-online-retailers",
    "https://www.pricklypages.com/2025/succullents/where-to-buy",
    "https://www.spinyliving.com/2025/latest-news"
  ]
}'
```

# Response

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status Code
      </th>

      <th>
        Response
      </th>

      <th>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Success**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        `{
          "success": true
        }`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Error**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
          "status":"error",
          "message/data":"<Specific to API>"
        }`
      </td>

      <td>
        Error with respect to API
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `{
          "status":"error",
          "message":"Unauthorized Access"
        }`
      </td>

      <td>
        When authentication fails
      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        `Too Many Requests`
      </td>

      <td>
        When rate limit is hit
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `{
          "status": "error",
          "message": "Internal Server Error"
        }`
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>

# Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Headers**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        PARTNER_APP_TOKEN
      </td>

      <td>
        Partner app access token issued post partner login
      </td>

      <td>
        Should be a valid Partner app access token belonging to the passed app ID
      </td>
    </tr>

    <tr>
      <td>
        **Request Params**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        business_website_url
      </td>

      <td>
        Business website of the brand
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        primary_country_of_operation
      </td>

      <td>
        Primary Country where the business operates
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        primary_language
      </td>

      <td>
        Primary language of the business
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        parent_business_or_brand
      </td>

      <td>
        Parent business or brand
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        supporting_links
      </td>

      <td>
        Articles in news or newspaper, blog posts or independent reviews that show your business is well known and recognized by consumers.
      </td>

      <td>
        Optional 

        Do not include the following: 

        - Your website

        - Your Facebook or Instagram page

        - Self-published, paid or promotional content
      </td>
    </tr>

    <tr>
      <td>
        additional_supporting_information
      </td>

      <td>
        Other information that may show your business is recognizable: here we can add how many followers they have in social media as Facebook and Instagram with the urls for each.
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        **Path Params**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        appId
      </td>

      <td>
        App ID for the app
      </td>

      <td>
        Valid app ID
      </td>
    </tr>
  </tbody>
</Table>

<br />