# Installation Guide
#### 1. Open your console (I use Powershell) and clone the repository:
`git clone https://github.com/kingco6ra/news_blog.git`
#### 2. Go to the project folder:
`cd .\news_blog\`
#### 3. Launch docker-compose:
`docker-compose up`
#### 4. Open a browser and visit 
`127.0.0.1:8000/`
#### Done. The API routes will be described below.

## To access the admin panel:
Login: **admin** <br>
Password: **admin**


---
- Python
- Django
- Django Rest Framework
- Docker

# API Endpoints:


| URL                                |    METHOD    |                                                        PERMISSIONS |DESCRIPTION|
| :----------------------------------- | :------------: | -------------------------------------------------------------------: | ----|
| api/                               |     GET     |                                                      **API root.** |API Navigation|
|                                    |              |                                                                    |
| api/news/                          |     GET     | **All users are allowed, including those who are not authorized.** |List of all news with hyper links to the author, category, comments|
| api/news/                          |     POST     |                             **Only authorized users are allowed.** |
| api/news/`id`/                        |   GET `and` PUT     |             **Editing is allowed only to the author of the post.** |Data of the selected news publication.|
|                                    |              |                                                                    |
| api/comments/                      |     GET     | **All users are allowed, including those who are not authorized.** |A list of all comments with hyperlinks to the author and the news post to which the comment has left.|
| api/comments/                      |     POST     | **All users are allowed, including those who are not authorized.** |
| api/comments/`id`/                    |     GET `and` PUT     |          **Editing is allowed only to the author of the comment.** |Data of the selected comment.|
|                                    |              |                                                                    |
| api/users/                         |     GET     |                  **Access is allowed only for the administrator.** |A list of all registered users. All their news publications and all comments.|
| api/users/                         |     POST     |                  **Access is allowed only for the administrator.** |
| api/users/`id`/                       |     GET `and` PUT     |                  **Access is allowed only for the administrator.** |Data of the selected user.|
|                                    |              |                                                                    |
| api/categories/                    |     GET     | **All users are allowed, including those who are not authorized.** |List of all categories and hyperlinks to all news with this category.|
| api/categories/                    |     POST     |                             **Only the administrator is allowed.** |
| api/categories/`id`/                  |     GET `and` PUT     |                             **Only the administrator is allowed.** |Data of the selected category.|
|                                    |              |                                                                    |
| api/auth/login/ `AND` api/auth/logout/ | GET `and` POST |                                                 **For all users.** |Login / logout|


## JSON format for example
- ### api/news/1
```
{
    "id": 1,
    "author": "http://127.0.0.1:8000/api/users/1/",
    "category": "http://127.0.0.1:8000/api/categories/1/",
    "created_at": "12:53:58 2022-05-12",
    "updated_at": "10:57:41 2022-05-21",
    "news_comments": [],
    "title": "Test news publication",
    "preview_content": "Test text teaser of the publication",
    "content": "Test content",
    "photo": null,
    "is_published": true
}
```
- ### api/comments/1
```
{
    "id": 1,
    "author": "http://127.0.0.1:8000/api/users/1/",
    "news": "http://127.0.0.1:8000/api/news/4/",
    "created_at": "12:55:18 2022-05-12",
    "content": "Test comment"
}
```
- ### api/categories/1
```
{
    "id": 1,
    "news_category": [],
    "title": "Test category"
}
```
- ### api/users/1
```
{
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "date_joined": "12:25:22 2022-05-12",
    "author_news": [
        "http://127.0.0.1:8000/api/news/6/",
        "http://127.0.0.1:8000/api/news/5/",
        "http://127.0.0.1:8000/api/news/4/",
        "http://127.0.0.1:8000/api/news/3/",
        "http://127.0.0.1:8000/api/news/2/",
        "http://127.0.0.1:8000/api/news/1/"
    ],
    "author_comments": [
        "http://127.0.0.1:8000/api/comments/1/"
    ]
}
```

### Authorization / Registration

![изображение](https://user-images.githubusercontent.com/101705791/166693352-dc620923-60c3-458f-b4cd-56ebacb1e439.png)

![изображение](https://user-images.githubusercontent.com/101705791/166693418-999ba778-198d-4656-9b31-f46be61a1d12.png)

### Commenting on each individual news (Possible without registration)

![изображение](https://user-images.githubusercontent.com/101705791/166693684-05f2e1f9-7849-498c-ae93-6e6d2fd24366.png)

### Adding news from the form on the site for authorized users

![изображение](https://user-images.githubusercontent.com/101705791/166693955-abbbbbc6-9d38-429c-abaf-5414736fad73.png)

### CKEditor

![изображение](https://user-images.githubusercontent.com/101705791/166694828-28a8bbf8-24fa-415f-8c55-318b5e7e530a.png)
