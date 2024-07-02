class Locator:
    def __init__(self, selector, page):
        self.selector = selector
        self.page = page


    def get_locator(self):
        return self.page.selector
