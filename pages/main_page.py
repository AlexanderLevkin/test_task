from locators import locators
from utils.allure_report_methods import attach_response_picture


class AuthPage:
    def __init__(self, browser):
        self.page = browser

    def login(self, username):
        self.page.goto(locators.site)
        self.page.get_by_placeholder(locators.email_field).click()
        self.page.get_by_placeholder(locators.email_field).fill(username)
        screenshot = self.page.screenshot(path='artifacts/screenshots/screenshot.png')
        attach_response_picture(screenshot, 'screenshot')

        # self.page.click("role=button", name=locators.enter_button)
        # self.page.click("role=button", name="Войти")
        # self.page.fill("placeholder=Логин или email", "login")
        # self.page.click("role=button", name="Войти")
        # self.page.fill("placeholder=Введите пароль", password)
        # self.page.click("role=button", name="Войти", exact=True)
