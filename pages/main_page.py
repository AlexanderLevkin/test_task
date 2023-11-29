from playwright.sync_api import expect
from utils.logger import logger
from locators import locators
from utils import handle_report_methods
import datetime


class AuthPage:
    def __init__(self, browser):
        self.page = browser

    # METHODS (Auxialiary)
    def capture_screenshot(self):
        screen_shot_name = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot_path = f"artifacts/screenshots/{screen_shot_name}"
        screenshot = self.page.screenshot(path=screenshot_path)
        handle_report_methods.attach_response_picture(screenshot, screen_shot_name)

    # GETTERS
    def common_code(self, field, value):
        field.click()
        field.fill(value)

    def login_field(self, username):
        email_field = self.page.get_by_placeholder(locators.email_field)
        self.page.goto(locators.site)
        self.common_code(email_field, username)
        email_field.press("Enter")

    def password_field(self, password):
        password_field = self.page.get_by_placeholder(locators.password_field)
        self.common_code(password_field, password)
        password_field.press("Enter")

    def phone_field(self, phone):
        self.page.goto(locators.site)
        self.page.get_by_role("button", name=locators.phone_button).click()
        phone_field = self.page.locator(locators.phone_field)
        self.common_code(phone_field, phone)
        phone_field.press("Enter")

    # ASSERTS
    def check_login_field(self):
        """Here we check that we are on the password page"""
        try:
            expect(self.page.get_by_placeholder(locators.password_field)).to_be_visible()
            logger.info("We are on the password page")

        except AssertionError as e:
            self.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def check_password_field_with_valid_password(self):
        """Here we check that the password functionality of password field"""
        try:
            expect(self.page.get_by_text(locators.wrong_password_message)).to_be_hidden()
            logger.info("Password field with valid password works correctly")

        except AssertionError as e:
            self.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def check_password_field_with_wrong_password(self):
        """Here we check that the password functionality of password field"""
        try:
            expect(self.page.get_by_text(locators.wrong_password_message)).to_be_visible()
            logger.info("Password field with wrong password works correctly")

        except AssertionError as e:
            self.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def check_entering_with_valid_phone(self):
        """Here we check how captcha after valid phone field works"""
        try:
            expect(self.page.get_by_label(locators.sms_message)).to_be_editable()
            logger.info("Phone field with valid phone works correctly")

        except AssertionError as e:
            self.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

    def check_with_invalid_phone(self):
        """Here we check how captcha after invalid phone field works"""
        try:
            expect(self.page.get_by_text(locators.wrong_phone_message)).to_be_visible()
            logger.info("Phone field with invalid phone works correctly")

        except AssertionError as e:
            self.capture_screenshot()
            handle_report_methods.handle_assertion_error(e)

