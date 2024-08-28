import time

import allure
import pytest

from assertions.assertions import Assertions
from locators import locators, credentials
from pages.casino_page import CasinoPage
from pages.main_page import AuthPage


@allure.feature("AUTHORIZATION PAGE")
@allure.title('Test with Login Field')
@allure.label('owner', 'Levkin.A')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("games", [("Play for funGates of Olympus", "#casino-game-game_544816-544816 iframe")],
                         ids=["Play for funGates of Olympus"])
def test_open_the_game(browser_context_args, games, request):
    ids = request.node.callspec.id.split('-')[-1].strip()
    with allure.step("Login with valid login and valid password"):
        auth_page = AuthPage(browser_context_args)
        auth_page.go_to_main_page(locators.url)
        auth_page.press_login_button()
        auth_page.fill_fields(locator=locators.login_field_locator, text=credentials.valid_login)
        auth_page.fill_fields(locator=locators.password_field_locator, text=credentials.valid_password)
        auth_page.press_login_button(is_popup=True)
    with allure.step("Find and open the particular game"):
        casino_page = CasinoPage(browser_context_args)
        casino_page.find_and_click_casino_button(locators.casino_button)
        casino_page.find_and_click_particular_game(games[0])
    with allure.step(f"Check that the game {ids} is opened"):
        assertions = Assertions(browser_context_args)
        assertions.is_it_visible(games[1])
