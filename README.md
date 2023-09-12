# Usage

clone the repository to your local machine

install requirements file

configure your database variables in the env file

create an sql database
 NB dont create tables

to run the database, use python3 app.py

# inserting a new user

```
 curl -X POST "http://localhost:5000/api?user_name=JohnDoe&user_email=johndoe@example.com"
 ```

# retrieving a user data using the user id
```
curl -X GET "http://localhost:5000/api/84650a8e53274bc5bf591e45f191fdea"
```


# deleting the user data based on the user id
```
curl -X DELETE "http://localhost:5000/api/84650a8e53274bc5bf591e45f191fdea"
```


# updating a user based on id

```
curl -X PUT -d "f_name=UpdatedName&user_email=updatedemail@example.com" "http://localhost:5000/api/cd53c9ee77f045cc83896338485b9285"
```




## How i have protected myself from common vulnerabilities
** use orm \n
** avoided using raw sql queries \\n
** i have used parameterized queries such as filter and first\n


### output

Creating a user

** On creating a user the response will be the user id which can be used for CRUD operations

```
samson@pc:~/hng-stage-two-crud$ curl -X POST "http://localhost:5000/api?f_name=John&l_name=Doe&user_email=johndoe@exampl.com"


"84650a8e53274bc5bf591e45f191fdea"


```

updating a user

** The response will be updated user

```
samson@pc:~/hng-stage-two-crud$ curl -X PUT -d "f_name=UpdatedName&l_name=sam&user_email=updatedemail@example.com" "http://localhost:5000/api/cd53c9ee77f045cc83896338485b9285"

{"email":"updatedemail@example.com","f_name":"UpdatedName","id":"cd53c9ee77f045cc83896338485b9285","l_name":"sam"}

```

getting a user

** Using the userid provided above, one can get the user of that id

```
samson@pc:~/hng-stage-two-crud$ curl -X GET "http://localhost:5000/api/84650a8e53274bc5bf591e45f191fdea"

{"email":"johndoe@exampl.com","f_name":"John","id":"84650a8e53274bc5bf591e45f191fdea","l_name":"Doe"}


```

deleting a user

** To delete a user, one can use the id from the post or get request

```
samson@pc:~/hng-stage-two-crud$ curl -X DELETE "http://localhost:5000/api/84650a8e53274bc5bf591e45f191fdea"

{"message":"user deleted"}

```
