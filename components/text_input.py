from components.locator import Locator


class TextInput(Locator):
    async def fill(self, text: str):
        await self.get_locator().fill(text)