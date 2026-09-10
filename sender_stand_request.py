import requests
import configuration

def get_stand_documentation():
    # Формируем полный URL, соединяя базовый URL и путь к документации
    url = configuration.URL_SERVICE + configuration.DOC_PATH
    
    # Отправляем GET-запрос
    response = requests.get(url)
    
    # Возвращаем статус-код ответа
    return response.status_code

# Проверяем, что всё работает
if __name__ == "__main__":
    status_code = get_stand_documentation()
    print(f"Статус-код ответа: {status_code}")