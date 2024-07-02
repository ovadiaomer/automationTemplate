class BasePage:
    def __init__(self, page):
        self._page = page

    def open(self, url):
        self._page.goto(url)
