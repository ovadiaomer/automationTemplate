from components.button import Button
from config.config import Config
from pages.base_page import BasePage

class ExamplePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.example_button = Button("text=Example Button", self._page)

    def open(self):
        super().open(Config.BASE_URL)
