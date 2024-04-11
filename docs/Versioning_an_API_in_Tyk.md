Versioning an OAS(OpenAPI Specification) API in Tyk using Postman.
 
Endpoint	Port	Auth Header	Credential
tyk/apis/oas	8080	x-tyk-authorization	‘secret’ – tyk.conf


1.	First you must create your Base api, this is like a regular api in tyk that acts like a request router by storing all other versions. Below is an example of the versioning settings within the Base api.
{
  "x-tyk-api-gateway": {
    "info": {
      "expiration": "{expiration-date}",
      "versioning": {
        "enabled": true,
        "name": "Default",
        "default": "self",
        "location": "header",
        "key": "version",
        "versions": [
          {
            "name": "v1",
            "apiId": "<version-api-id>"
          },
          {
            "name": "v1",
            "apiId": "<version-api-id>"
          }
        ],
        "stripVersioningData": false
      }
    }
  }
}
-	Creating minimal base api here in postman. I am using httpbin as my base apis upstream url

