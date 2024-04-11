Enabling and Creating a Basic Authentication User in Tyk

1.	To enable Basic Authentication, the API Definition file needs to be set up to allow basic authentication, this is achieved by setting use_basic_auth to true:
```   
{
  "use_basic_auth": true,
}
```
<img width="450" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/45fedadd-a55a-4bf3-9f30-2c7cffb34095">


3.	Next reload your gateway since you have just added a new API
<img width="450" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/97a173dd-cddd-4fca-89cc-d66d0672373c">

4.	Next create a new basic authentication user in Tyk. Ensure that org_id is set correctly and consistently so the user is in the correct organization.

| Method | Endpoint | Header |
|----------|----------|----------|
| POST | tyk/keys | ‘secret’ – tyk.conf |


After the endpoint tyk/keys/{username} is the username of the authenticated user. Also you will notice how I have added this user to the correct organization and included my api-id : “validauth” and name : “ValidUser” from step 1. 
<img width="468" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/14888d18-9265-4cb7-86d6-58d031ff70de">




Here I am sending a request to the authenticated endpoint with my newly created username and password encoded.
<img width="532" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/7d7c8cfe-d3af-4f0d-9e9d-6105ef5c96f2">

