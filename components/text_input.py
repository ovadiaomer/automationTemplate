class TextInput:
    def __init__(self, locator, page):
        self.locator = locator
        self.page = page

    def type(self, text):
        self.page.fill(self.locator, text)
