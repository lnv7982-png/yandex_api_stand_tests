import requests
import configuration


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


if __name__ == "__main__":
    response = get_users_table()
    print(response.status_code)