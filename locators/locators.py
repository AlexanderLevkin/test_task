import json
from api.http_methods import method_get

response = (method_get("https://jsonplaceholder.typicode.com/users", None))
response_data = json.loads(response.text)

# URLS
url_after_enter_login = "https://passport.yandex.ru/auth/welcome?retpath=https%3A%2F%2Fpassport.yandex.ru%2F&noreturn=1"
site = "https://passport.yandex.ru/"

# Locators
valid_login = "example"
valid_password = "12345678"  # Here should be the valid password (now this is fake)
valid_phone = "+375(33)337-15-31"
invalid_login, invalid_password, invalid_phone = (response_data[0]['email'], response_data[0]['website'],
                                                  response_data[0]['phone'])
email_field = "Логин или email"
password_field = "Введите пароль"
phone_button = "Телефон"
phone_field = "#passp-field-phone"
enter_button = "Войти"

# Messages
wrong_login_message = "Такой логин не подойдет"
wrong_password_message = "Неверный пароль"
wrong_phone_message = "Недопустимый формат номера"

sms_message = "Введите код"
