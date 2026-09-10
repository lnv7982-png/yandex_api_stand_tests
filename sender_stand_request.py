import requests
import configuration


def get_logs():
    """
    Функция отправляет GET-запрос к серверу для получения логов.
    Возвращает ответ от сервера.
    """
    # Формируем полный URL, соединяя базовый URL и путь к логам
    url = configuration.URL_SERVICE + configuration.LOG_MAIN_PATH
    
    # Отправляем GET-запрос
    response = requests.get(url)
    
    # Возвращаем ответ
    return response


# Проверяем, что всё работает
if __name__ == "__main__":
    response = get_logs()
    
    # Выводим статус-код ответа
    print(f"Статус-код ответа: {response.status_code}")
    
    # Выводим заголовки ответа
    print(f"Заголовки ответа: {response.headers}")