from playwright.sync_api import Page, Locator as PlaywrightLocator

class Locator:
    def __init__(self, selector: str, page: Page):
        self.selector = selector
        self.page = page

    def get_locator(self) -> PlaywrightLocator:
        return self.page.locator(self.selector)

    async def wait_for(self, state: str = "attached"):
        await self.get_locator().wait_for(state=state)
