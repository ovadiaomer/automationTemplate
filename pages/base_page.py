from playwright.sync_api import Page

from components.locator import Locator


class BasePage:
    def __init__(self, page: Page):
        self._page: Page = page

    def open(self, url):
        self._page.goto(url)
        self.verify_page_loaded()

    def verify_page_loaded(self):
        # Use the overridden common_locator if available in the derived class
        wait_for_locator: Locator = getattr(self, 'common_locator', self.wait_for_locator)
        wait_for_locator.get_locator().nth(0).wait_for(state="attached")
