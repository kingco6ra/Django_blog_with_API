- Python
- Django
- Django Rest Framework

### API Endpoints:
|URL|METHOD|PERMISSIONS|
|:--|:----:|      ---: |
|api/|GET|**API root.**|
|||
|api/news/|GET|**All users are allowed, including those who are not authorized.**|
|api/news/|POST|**Only authorized users are allowed.**|
|api/news/i/|PUT|**Editing is allowed only to the author of the post.**|
|||
|api/comments/|GET|**All users are allowed, including those who are not authorized.**|
|api/comments/|POST|**All users are allowed, including those who are not authorized.**|
|api/comments/i/|PUT|**Editing is allowed only to the author of the comment.**|
|||
|api/users/|GET|**Access is allowed only for the administrator.**|
|api/users/|POST|**Access is allowed only for the administrator.**|
|api/users/i/|PUT|**Access is allowed only for the administrator.**|
|||
|api/categories/|GET|**All users are allowed, including those who are not authorized.**|
|api/categories/|POST|**Only the administrator is allowed.**|
|api/categories/i/|PUT|**Only the administrator is allowed.**|
|||
|api/authlogin/ AND api/authlogout/|GET and POST|**For all users.**|


### Authorization / Registration

![изображение](https://user-images.githubusercontent.com/101705791/166693352-dc620923-60c3-458f-b4cd-56ebacb1e439.png)

![изображение](https://user-images.githubusercontent.com/101705791/166693418-999ba778-198d-4656-9b31-f46be61a1d12.png)

### Commenting on each individual news (Possible without registration)

![изображение](https://user-images.githubusercontent.com/101705791/166693684-05f2e1f9-7849-498c-ae93-6e6d2fd24366.png)

### Adding news from the form on the site for authorized users

![изображение](https://user-images.githubusercontent.com/101705791/166693955-abbbbbc6-9d38-429c-abaf-5414736fad73.png)

### CKEditor

![изображение](https://user-images.githubusercontent.com/101705791/166694828-28a8bbf8-24fa-415f-8c55-318b5e7e530a.png)



