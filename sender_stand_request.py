# Импорт настроек из модуля configuration
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data (заголовки и тело запроса)
import data


# Функция для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Вызов функции post_new_user с телом запроса из модуля data
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
print(response.status_code)
print(response.json())