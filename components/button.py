from components.locator import Locator


class Button(Locator):
    # def __init__(self, locator, page):
    #     self.locator = locator
    #     self.page = page

    async def click(self):
        await self.get_locator().click()
