import requests
import configuration
import data
# Функция для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids)


# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.products_ids)

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
print(response.status_code)
print(response.json())