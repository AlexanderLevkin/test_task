import allure
import pytest

from locators import locators
from pages.main_page import AuthPage
from utils.logger import logger


@allure.feature("AUTHORIZATION PAGE")
@allure.title('Test with Login Field')
@allure.label('owner', 'Levkin.A')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login, password", [(locators.login, locators.password),
                                             (locators.invalid_login, locators.password),
                                             (locators.login, locators.invalid_password),
                                             (locators.invalid_login, locators.invalid_password)],
                         ids=["Test login with valid login and password",
                              "Test login with invalid login and correct password",
                              "Test login with valid login and invalid password",
                              "Test login with invalid login and invalid password",])
def test_authorization_with_email(browser_context_args, trace_file_cleaning, login, password):
    with allure.step("Open main page"):
        enter_the_login = AuthPage(browser_context_args)
        logger.info("Main page was opened successfully")

    with allure.step("Enter Login"):
        enter_the_login.login_field(login)

    with allure.step("Check Transfer to the password page"):
        enter_the_login.check_login_field()

    with allure.step("Enter Password"):
        enter_the_login.password_field(password)

    with allure.step("Check Password is wrong"):
        enter_the_login.check_password_field()


@allure.feature("AUTHORIZATION PAGE")
@allure.title('Test with Phone Field')
@allure.label('owner', 'Levkin.A')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login, password", [(locators.phone, locators.password),
                                             (locators.invalid_phone, locators.password),
                                             (locators.phone, locators.invalid_password),
                                             (locators.invalid_phone, locators.invalid_password)],
                         ids=["Test login with valid phone and password",
                              "Test login with invalid phone and correct password",
                              "Test login with valid phone and invalid password",
                              "Test login with invalid phone and invalid password",])
def test_authorization_with_email(browser_context_args, trace_file_cleaning, phone, password):
    with allure.step("Open main page"):
        enter_the_login = AuthPage(browser_context_args)
        logger.info("Main page was opened successfully")

    with allure.step("Enter Phone number"):
        enter_the_login.phone_field(phone)

    with allure.step("Check Transfer to the password page"):
        enter_the_login.check_login_field()

    with allure.step("Enter Password"):
        enter_the_login.password_field(password)

    with allure.step("Check Password is wrong"):
        enter_the_login.check_password_field()
