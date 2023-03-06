# self-tracker
This is application which tracks all your personal things ;)

# Tech Used
- Python 3.10
- Flask
- Pydantic
- Sqlite3 (temp)

# Installation Steps

### Normal Python Installtion
1. Verify python version
    > python -V # python3.10

2. Install poetry
    > pip install poetry

3. Install dependencies using poetry
    > poetry install

# Endpoints
Below are the endpoints, expected response body and params and returned response. Currently using version 1 of api with API prefix as `/api/v1`

### Status
> GET /health

_Check application health status_
```
Status Code: 200
Response: "OK"
```

### User
> POST /user

_Add a new user_
```
Request:
  {
      "first_name": "pratik",
      "last_name": "ghodke",
      "email": "pratik@outlook.com",
      "mobile": "123123123",
      "birth_date": "2001-01-16",
      "password": "password"
  }
```

```
Status Code: 201
Response:
  {
      "created_at": "2023-03-06T08:50:09",
      "email": "pratik@outlook.com",
      "id": 1,
      "mobile": "1231231231",
      "name": "pratik ghodke",
      "updated_at": "2023-03-06T08:50:09"
  }

ERROR RESPONSE

Status Code: 400
Response:
  {
      "message": "User with same email OR mobile already exists",
      "status": "FAILED"
  }
```

<hr>

> GET /user

_Get list of users_
```
Query Params:
  page=1
  items_per_page=10
```
```
Status Code: 200
Response:
  [list of users]
```

<hr>

> GET /user/<user_id: int>

_Get a single user by ID_
```
URL params:
  user_id (int)
```
```
Status Code: 200
Response:
{
    "created_at": "2023-03-06T08:50:09",
    "email": "pratik@outlook.com",
    "id": 1,
    "mobile": "1231231231",
    "name": "pratik ghodke",
    "updated_at": "2023-03-06T08:50:09"
}

ERROR RESPONSE

Status Code: 404
Response:
{
    "message": "User [112] does not exists",
    "status": "FAILED"
}
```

<hr>

> PUT /user/<user_id: int>

_Update a user by ID_
```
URL params:
  user_id (int)

Request (all optional):
  {
      "first_name": "pratik",
      "last_name": "ghodke",
      "email": "pratik@outlook.com",
      "mobile": "123123123",
      "birth_date": "2001-01-16",
      "password": "password"
  }
```

```
Status Code: 200
Response:
  {
      "message": "Updated User [1]",
      "status": "SUCCESS"
  }

ERROR RESPONSE

Status Code: 404
Response:
  {
      "message": "User [112] does not exists",
      "status": "FAILED"
  }
```

<hr>

> DELETE /user/<user_id: int>

_Delete a user by ID_
```
URL params:
  user_id (int)
```

```
Status Code: 204

ERROR RESPONSE

Status Code: 404
Response:
  {
      "message": "User [112] does not exists",
      "status": "FAILED"
  }
```
