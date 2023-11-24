import allure
from locators import locators
from pages.main_page import AuthPage
from utils.logger import logger


def test_checkbox_with_click(browser_context_args):
    with allure.step("Open main page"):
        enter_the_login = AuthPage(browser_context_args)
        logger.info("Main page was opened successfully")

    with allure.step("Enter Login"):
        enter_the_login.login(locators.login)
        logger.info("Enter Login was successful")
