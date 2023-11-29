import allure
import pytest

from locators import locators
from pages.main_page import AuthPage
from utils.logger import logger


@allure.feature("AUTHORIZATION PAGE")
@allure.title('Test with Login Field')
@allure.label('owner', 'Levkin.A')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login, password", [(locators.valid_login, locators.valid_password),
                                             (locators.valid_login, locators.invalid_password),
                                             (locators.invalid_login, locators.invalid_password)],
                         ids=["Test login with valid login and valid password",
                              "Test login with valid login and invalid password",
                              "Test with invalid login and invalid password"])
def test_authorization_with_email(browser_context_args, trace_file_cleaning, login, password):
    with allure.step("Open main page"):
        enter_the_login = AuthPage(browser_context_args)
        logger.info("Main page was opened successfully")

    with allure.step("Enter Login"):
        enter_the_login.login_field(login)

    with allure.step("Check Login field"):
        enter_the_login.check_login_field()

    if password == locators.valid_password:

        with allure.step("Enter Password"):
            enter_the_login.password_field(password)

        with allure.step("Check Password is wrong"):
            enter_the_login.check_password_field_with_valid_password()

    elif password == locators.invalid_login:
        with allure.step("Enter Password"):
            enter_the_login.password_field(password)

        with allure.step("Check Password is wrong"):
            enter_the_login.check_password_field_with_wrong_password()


@allure.feature("AUTHORIZATION PAGE")
@allure.title('Test with Phone Field')
@allure.label('owner', 'Levkin.A')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("phone", [locators.valid_phone,
                                   locators.invalid_phone],
                         ids=["Test login with valid phone",
                              "Test login with invalid phone", ])
def test_authorization_with_phone(browser_context_args, trace_file_cleaning, phone):
    with allure.step("Open main page"):
        enter_the_phone = AuthPage(browser_context_args)
        logger.info("Main page was opened successfully")

    with allure.step("Enter Phone number"):
        enter_the_phone.phone_field(phone)

    if phone == locators.valid_phone:

        with allure.step("Check Password is wrong"):
            enter_the_phone.check_entering_with_valid_phone()

    elif phone == locators.invalid_phone:

        with allure.step("Check Password is wrong"):
            enter_the_phone.check_with_invalid_phone()
