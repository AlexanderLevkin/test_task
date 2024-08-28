import re
from utils import handle_report_methods
from assertions.assertions import Assertions
import datetime


class AuthPage:
    def __init__(self, browser):
        self.page = browser
        self.assertions = Assertions(browser)

    def fill_fields(self, locator, text):
        try:
            login_field = self.page.locator(locator)
            login_field.fill(text)
        except Exception as e:
            self.assertions.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def go_to_main_page(self, url):
        try:
            self.page.goto(url)
        except Exception as e:
            self.assertions.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def press_login_button(self, is_popup=False):
        try:
            if is_popup:
                self.page.locator(".Dialog__actions > div").first.click()
            else:
                self.page.locator("div").filter(has_text=re.compile(r"^Login$")).first.click()
        except Exception as e:
            self.assertions.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)
