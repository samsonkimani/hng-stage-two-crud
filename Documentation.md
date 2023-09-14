### 1. Using Curl to Send a POST Request to Create a User

In this example, we'll demonstrate how to use the `curl` command to send a POST request to the `/api` endpoint of your API to create a user. We'll include both `user_name` and `user_email` as JSON data in the request body.

## Curl Command

```bash
curl -X POST -H "Content-Type: application/json" -d '{"user_name": "JohnDoe", "user_email": "johndoe@example.com"}' "https://hng-stage-two-crud.onrender.com/api"

```

## Server response
 A user id is returned

```
samson@pc:~/hng-stage-two-crud$ curl -X POST -H "Content-Type: application/json" -d '{"user_name": "JohnDoe", "user_email": "johndoe@example.com"}' "https://hng-stage-two-crud.onrender.com/api"

"f52d8dfcac0f4885a40f2791c42d6dc6"
```

### 2. Using Curl to Send a GET Request to Get User by ID

In this example, we'll demonstrate how to use the `curl` command to send a GET request to the `/api/<user_id>` endpoint of your API to retrieve a user by their ID.

## Curl Command

```bash
curl -X GET "https://hng-stage-two-crud.onrender.com/api/<user_id>"
```



### 3. Update User by ID

```markdown
# Using Curl to Send a PUT Request to Update User by ID


In this example, we'll demonstrate how to use the `curl` command to send a PUT request to the `/api/<user_id>` endpoint of your API to update a user's information by their ID.
```
## Curl Command

```bash
curl -X PUT -d "user_name=UpdatedName" -d "user_email=updated.email@example.com" "https://hng-stage-two-crud.onrender.com/api/<user_id>"
```


### 4. Delete User by ID

```markdown
# Using Curl to Send a DELETE Request to Delete User by ID

In this example, we'll demonstrate how to use the `curl` command to send a DELETE request to the `/api/<user_id>` endpoint of your API to delete a user by their ID.
```

## Curl Command


```bash
curl -X DELETE "https://hng-stage-two-crud.onrender.com/api<user_id>"
```
