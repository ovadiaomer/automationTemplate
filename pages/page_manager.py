from typing import Optional, Dict, Type
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.playwright_page import PlaywrightPage

class PageManager:
    def __init__(self, page: Page):
        self._page: Page = page
        self._pages: Dict[str, Optional[BasePage]] = {
            "playwright_page": None,
            "example_page": None,
            "main_page": None
        }

    @property
    def page(self) -> Page:
        return self._page

    def get_page(self, page_name: str, page_class: Type[BasePage]) -> BasePage:
        if self._pages[page_name] is None:
            self._pages[page_name] = page_class(self.page)
        return self._pages[page_name]

    def back(self):
        self._page.go_back()
        self.parent.loader_circle.wait_for(state="hidden")

    @property
    def playwright_page(self) -> PlaywrightPage:
        return self.get_page("playwright_page", PlaywrightPage)

    @property
    def main_page(self) -> MainPage:
        return self.get_page("main_page", MainPage)

    def close(self):
        self._page.close()
