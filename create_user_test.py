import sender_stand_request
import data


# Эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Функция для негативной проверки
# В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)

    print(f"Код ответа: {response.status_code}")
    print(f"Всё тело ответа: {response.json()}")
    print(f"Сообщение из ответа: {response.json()['message']}")

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Функция для негативной проверки кода ответа
def negative_assert_status_code(user_body, expected_code):
    response = sender_stand_request.post_new_user(user_body)
    
    print(f"Код ответа: {response.status_code}")
    print(f"Ожидаемый код: {expected_code}")
    
    assert response.status_code == expected_code


# Тест 12. Ошибка
# Тип параметра firstName: число
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    negative_assert_status_code(user_body, 400)


# Запускаем тест 12
test_create_user_number_type_first_name_get_error_response()
print("✓ Тест 12 (число в firstName) пройден успешно!")