# SAP-SimpleAuthenticationProvider
SAP - Simple Authentication Provider is the REST API that help you to test or use in simple authentication with API for your simple project.

# How to request for login : 
``` 
curl -X POST -H "Content-Type: application/json" \
    -d '{"username": "[username]", "password": "[password]"}' \
    https://simpleauthenticationprovider.herokuapp.com/login
```

# How to request for signup : 
``` 
curl -X POST -H "Content-Type: application/json" \
    -d '{"username": "[username]", "password": "[password]"}' \
    https://simpleauthenticationprovider.herokuapp.com/signup
```

All of those request will have the response type as :
```
{
  "status" : [status code],
  "message" : [message from server]
}
```
Except when we login successfully, we will also get the uid of the user.
```
{
  "status" : [status code],
  "message" : [message from server],
  "uid" : [uid number]
}
```

Please raise the issue if you have any question.
