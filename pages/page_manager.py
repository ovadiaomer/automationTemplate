from typing import Optional, Dict, Type

from playwright.sync_api import Browser, Page

from pages.base_page import BasePage
from pages.example_page import ExamplePage
from pages.playwright_page import PlaywrightPage


class PageManager:
    def __init__(self, browser: Browser):
        self.browser: Browser = browser
        self._page: Optional[Page] = None
        self._pages: Dict[str, Optional[BasePage]] = {
            "playwright_page": None,
            "example_page": None
        }

    @property
    def page(self) -> Page:
        if self._page is None:
            self._page = self.browser.new_page()
        return self._page

    def get_page(self, page_name: str, page_class: Type[BasePage]) -> BasePage:
        if self._pages[page_name] is None:
            self._pages[page_name] = page_class(self.page)
        return self._pages[page_name]

    @property
    def playwright_page(self) -> PlaywrightPage:
        return self.get_page("playwright_page", PlaywrightPage)

    @property
    def example_page(self) -> ExamplePage:
        return self.get_page("example_page", ExamplePage)

    def close(self):
        if self._page is not None:
            self._page.close()
