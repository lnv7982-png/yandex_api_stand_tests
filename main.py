import requests

response = requests.get('https://ya.ru')
print(f'Статус-код: {response.status_code}')
print(f'Первые 100 символов: {response.text[:100]}')