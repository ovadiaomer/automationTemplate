from components.button import Button
from config.config import Config
from pages.base_page import BasePage

class PlaywrightPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.get_started_button = Button("text=Get started", self._page)

    def open(self):
        super().open(Config.BASE_URL)
