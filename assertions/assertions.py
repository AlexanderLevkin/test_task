from playwright.sync_api import expect

from utils import handle_report_methods
import datetime


class Assertions:
    def __init__(self, browser):
        self.page = browser

    def capture_screenshot(self):
        screen_shot_name = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot_path = f"artifacts/screenshots/{screen_shot_name}"
        screenshot = self.page.screenshot(path=screenshot_path)
        handle_report_methods.attach_response_picture(screenshot, screen_shot_name)

    def is_it_visible(self, game_locator):
        expect(self.page.frame_locator(game_locator).locator("#game canvas")).to_be_visible()
