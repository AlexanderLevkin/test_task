from playwright.sync_api import expect
from utils.logger import logger
from locators import locators
from utils import handle_report_methods


class AuthPage:
    def __init__(self, browser):
        self.page = browser

    # GETTERS
    def common_code(self, field, value):
        field.click()
        field.fill(value)
        screenshot = self.page.screenshot(path='artifacts/screenshots/screenshot.png')
        handle_report_methods.attach_response_picture(screenshot, 'screenshot')
        self.page.get_by_role("button", name=locators.enter_button).click()

    def login_field(self, username):
        email_field = self.page.get_by_placeholder(locators.email_field)
        self.page.goto(locators.site)
        self.common_code(email_field, username)

    def password_field(self, password):
        password_field = self.page.get_by_placeholder(locators.password_field)
        self.common_code(password_field, password)

    def phone_field(self, phone):
        self.page.get_by_role("button", name=locators.phone_button).click()
        self.page.locator(locators.phone_field).click()
        self.page.locator(locators.phone_field).fill(phone)
        self.page.get_by_role("button", name=locators.enter_button).click()

        expect(self.page.get_by_text("Недопустимый формат номера")).to_be_visible()

    # ASSERTS
    def check_login_field(self):
        """Here we check that we are on the password page"""
        try:
            expect(self.page.get_by_placeholder(locators.password_field)).to_be_visible()
            logger.info("We are on the password page")

        except AssertionError as e:
            handle_report_methods.handle_assertion_error(e)

    def check_password_field(self):
        """Here we check that the password functionality of password field"""
        try:
            expect(self.page.get_by_text(locators.wrong_password_message)).to_be_visible()
            logger.info("Password fild works correctly")

        except AssertionError as e:
            handle_report_methods.handle_assertion_error(e)

    def check_phone_field(self):
        """Here we check how phone field works"""
        try:
            expect(self.page.get_by_text(locators.wrong_phone_message)).to_be_visible()
            logger.info("Phone fild works correctly")

        except AssertionError as e:
            handle_report_methods.handle_assertion_error(e)