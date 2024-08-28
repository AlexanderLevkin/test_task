from assertions.assertions import Assertions
from utils import handle_report_methods
import datetime


class CasinoPage:
    def __init__(self, browser):
        self.page = browser
        self.assertions = Assertions(browser)

    def find_and_click_casino_button(self, locator):
        try:
            self.page.locator(locator).first.click()
        except Exception as e:
            self.assertions.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def find_and_click_particular_game(self, locator):
        try:
            self.page.locator(locator).click()
        except Exception as e:
            self.assertions.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)
