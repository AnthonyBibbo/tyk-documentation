//Header: x-tyk-authorization 
This header is used a lot. The value is stored in the ‘secret’ property of the tyk.conf file

1.	Ensure Tyk is up and running by hitting the /hello endpoint.
http://{your-tyk-host}:{port}/hello 
<img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/2bcc83cf-db1a-4379-a3a5-4aaffd8eaf1b">

2.	Send a POST request with an api definition to the /tyk/apis endpoint on your gateway with the following headers. x-tyk-authorization: {your-secret} and Content-Type: application/json. This should look something like 

//must have…
-	Unique “api_id” value
-	“listen_path” this is what you are naming your endpoint
-	“target_url” the upstream service tyk will reverse proxy the request to
<img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/2ffcc7e3-f6cf-4c49-85cf-c1766a5d23e4">

3.	Reload the gateway by sending get request with x-tyk-authorization header to the tyk/reload endpoint.
<img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/e697ce3d-fb68-4531-a5b9-33e89354bfa2">

4.	You can now test the newly created api by sending a get request to the endpoint with you x-tyk-authorization header. My target url https://jsonplaceholder.typicode.com has the endpoint /todos/1 already set up. So, you can see here when I hit my new api with /todos/1 appended to the end it will return the correct response. 
<img width="400" alt="image" src="https://github.com/AnthonyBibbo/tyk-documentation/assets/118140090/fc670185-4002-4baa-bc03-89727bbb8b13">
