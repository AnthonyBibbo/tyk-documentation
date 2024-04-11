Versioning an OAS(OpenAPI Specification) API in Tyk using Postman.

 | Endpoint | Port | Auth Header | Credential |
|----------|----------|----------|------------|
| tyk/apis/oas | 8080 | x-tyk-authorization | ‘secret’ – tyk.conf |



1.	First you must create your Base api, this is like a regular api in tyk that acts like a request router by storing all other versions. Below is an example of the versioning settings within the Base api.

```JSON
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
```

-	Creating minimal base api here in postman. I am using httpbin as my base apis upstream url
  <img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/a7fb3b6c-a8e4-40ec-a6c0-e77fea4ca5ca">

2.	Always remember to reload your gateway after creating a new API!
<img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/ee3ede6c-3aff-48b0-99a8-01dbe3400624">

3.	Create a new version of your API. This time I will be using https://jsonplaceholder.typicode.com as the upstream url. 

| Endpoint | Method | Parameters | 
|----------|----------|----------|
| tyk/apis/oas | POST | base_api_id : The API ID of the Base API to which the new version will be linked. <br>base_api_version_name : The version name of the base API while creating the first version. This doesn’t have to be sent for the next versions but if it is set, it will override the base API version name. <br>new_version_name : The version name of the created version. <br>set_default : If true, the new version is set as default version. |
	 
<img width="500" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/dd3215f8-b809-40c9-8e25-7429ffc65973">

4.	Don’t forget to reload the gateway! /tyk/reload

5.	By sending a GET request to http://{your-tyk-host}:{port}/tyk/apis/oas/{API-ID} you will see a response to the upstream URL of your newly created versioned api.

6.	Testing: When I send a GET request to my second-api (upstream url: JsonPlaceholder) and pass in the header x-tyk-version : v1 then it will be rerouted to the Base api (upstream url: httpbin) 

<img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/92d6ef68-55b8-48bf-9433-93e49855dfb7">


