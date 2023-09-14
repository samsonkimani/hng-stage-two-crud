### 1. Using Curl to Send a POST Request to Create a User

In this example, we'll demonstrate how to use the `curl` command to send a POST request to the `/api` endpoint of your API to create a user. We'll include both `user_name` and `user_email` as JSON data in the request body.

## Curl Command

```bash
curl -X POST -F "user_name=John Doe" -F "user_email=johnkimanijkhfjs.com" "https://hng-stage-two-crud.onrender.com/api"

```

## Server response
 A user id is returned

```
samson@pc:~/hng-stage-two-crud$ curl -X POST -F "user_name=John Doe" -F "user_email=johnkimanijkhfjs.com" "https://hng-stage-two-crud.onrender.com/api"

"1b6b10f048c747ecafc956160e5b044c"
"
```

### 2. Using Curl to Send a GET Request to Get User by ID

In this example, we'll demonstrate how to use the `curl` command to send a GET request to the `/api/<user_id>` endpoint of your API to retrieve a user by their ID.

## Curl Command

```bash
curl -X GET "https://hng-stage-two-crud.onrender.com/api/<user_id>"
```

getting the user data
```
samson@pc:~/hng-stage-two-crud$ curl -X GET "https://hng-stage-two-crud.onrender.com/api/1b6b10f048c747ecafc956160e5b044c"

{"email":"johnkimanijkhfjs.com","id":"1b6b10f048c747ecafc956160e5b044c","user_name":"John Doe"}
```


### 3. Update User by ID

```markdown
# Using Curl to Send a PUT Request to Update User by ID


In this example, we'll demonstrate how to use the `curl` command to send a PUT request to the `/api/<user_id>` endpoint of your API to update a user's information by their ID.
```
## Curl Command

```bash
samson@pc:~/hng-stage-two-crud$ curl -X PUT -F "user_name=NEW.user" -F "user_email=johnkima.new.com" "https://hng-stage-two-crud.onrender.com/api/1b6b10f048c747ecafc956160e5b044c"

{"email":"johnkima.new.com","id":"1b6b10f048c747ecafc956160e5b044c","user_name":"NEW.user"}


```


### 4. Delete User by ID

```markdown
# Using Curl to Send a DELETE Request to Delete User by ID

In this example, we'll demonstrate how to use the `curl` command to send a DELETE request to the `/api/<user_id>` endpoint of your API to delete a user by their ID.
```

## Curl Command


```bash
samson@pc:~/hng-stage-two-crud$ curl -X DELETE "https://hng-stage-two-crud.onrender.com/api/1b6b10f048c747ecafc956160e5b044c"

{"message":"user deleted"}

```
