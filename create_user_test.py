import sender_stand_request
import data


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Тест 1. Успешное создание пользователя
# Параметр firstName состоит из 2 символов
def test_create_user_with_2_letter_first_name_gets_201_and_auth_token():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    print(f"Код ответа: {user_response.status_code}")
    print(f"Тело ответа: {user_response.text}")

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1


test_create_user_with_2_letter_first_name_gets_201_and_auth_token()
print("✓ Тест 1 пройден успешно!")