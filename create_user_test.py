import sender_stand_request
import data


# Эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Функция для негативной проверки
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 2 и не более 15 символов"


# Тест 8. Ошибка
# Параметр firstName состоит из строки спецсимволов
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")


# Запускаем тест 8
test_create_user_has_special_symbol_in_first_name_get_error_response()
print("✓ Негативный тест 8 (спецсимволы в имени) пройден успешно!")