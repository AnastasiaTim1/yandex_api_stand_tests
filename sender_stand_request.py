import requests
import configuration
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);

print(response.status_code)
print(response.json())