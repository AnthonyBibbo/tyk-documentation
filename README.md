# tyk-documentation
Compiled all documentation over the semester into one repository

Tyk Gateway (OSS) Documentation


Documentation I have found helpful:

	//List of Tyk gateway api endpoints intended for internal automation and integration
	https://tyk.io/docs/tyk-gateway-api/

	//Documentation for creating an api in Tyk
	https://tyk.io/docs/getting-started/create-api/

	//Documentation for versioning an api in Tyk
	https://tyk.io/docs/getting-started/using-oas-definitions/versioning-an-oas-api/
	
	//Basic auth documentation for Tyk
	https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/basic-auth/
	
Creating APIs in Tyk using Postman 
//Header: x-tyk-authorization 
This header is used a lot. The value is stored in the ‘secret’ property of the tyk.conf file

1.	Ensure Tyk is up and running by hitting the /hello endpoint.
http://{your-tyk-host}:{port}/hello 
<img width="250" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/5010e900-b689-4264-bc02-c447fc8c9964">


2.	Send a POST request with an api definition to the /tyk/apis endpoint on your gateway with the following headers. x-tyk-authorization: {your-secret} and Content-Type: application/json. This should look something like 

//must have…
-	Unique “api_id” value
-	“listen_path” this is what you are naming your endpoint
-	“target_url” the upstream service tyk will reverse proxy the request to
<img width="300" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/abe90be7-5c65-4373-865d-f66965112e49">


3.	Reload the gateway by sending get request with x-tyk-authorization header to the tyk/reload endpoint.
<img width="244" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/6a4fdc59-2231-4a1c-8b98-e9769603da7a">


4.	You can now test the newly created api by sending a get request to the endpoint with you x-tyk-authorization header. My target url https://jsonplaceholder.typicode.com has the endpoint /todos/1 already set up. So, you can see here when I hit my new api with /todos/1 appended to the end it will return the correct response. 
<img width="242" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/0ab6b54f-8605-4430-b364-31700f681875">


Versioning APIs in Tyk using Postman 

1.	

