# FastAPI
## Version: 0.1.0

### /

#### GET
##### Summary:

Get Todos

#### Preview

![Screenshot (265)](https://github.com/PritamSarbajna/fastapi-todo-api/assets/90236635/ab0690f8-aaa0-4ae7-a3e8-2f0a2d7d4379)

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

#### POST
##### Summary:

Post Todo

#### Preview 

![Screenshot (266)](https://github.com/PritamSarbajna/fastapi-todo-api/assets/90236635/61c54e4b-4f01-44a7-a868-c9bf9531b44d)

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /{id}

#### GET
##### Summary:

Get Todo

#### Preview 

![Screenshot (267)](https://github.com/PritamSarbajna/fastapi-todo-api/assets/90236635/bfca6209-5106-4c78-a618-c87b651b312b)

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### PUT
##### Summary:

Update Todo

### Preview

![Screenshot (268)](https://github.com/PritamSarbajna/fastapi-todo-api/assets/90236635/359ee191-8208-48dc-b3ce-1042ca5ad5bf)

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### DELETE
##### Summary:

Delete Todo

#### Preview

![Screenshot (269)](https://github.com/PritamSarbajna/fastapi-todo-api/assets/90236635/9dbc5524-4680-4985-a390-e5a4dd1243ab)

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
