import json
import os
from api.http_methods import method_get

response = (method_get("https://jsonplaceholder.typicode.com/users", None))
response_data = json.loads(response.text)


login, password = response_data[0]['email'], response_data[0]['website']

email_field = "Логин или email"
password_field = "Введите пароль"
site = "https://passport.yandex.ru/"
enter_button = "Войти"
