class Button:
    def __init__(self, locator, page):
        self.locator = locator
        self.page = page

    def click(self):
        self.page.click(self.locator)
