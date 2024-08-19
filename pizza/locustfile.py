import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.page_manager import PageManager
from locust import HttpUser, task, between
from playwright.async_api import async_playwright
import asyncio

class PlaywrightUser(HttpUser):
    wait_time = between(1, 3)
    playwright = None
    browser = None
    page = None
    _task = None

    async def on_start(self):
        print("b1 - on_start: Starting Playwright")
        self.playwright = await async_playwright().start()
        print("b2 - on_start: Launching browser")
        self.browser = await self.playwright.chromium.launch(headless=False)
        print("b3 - on_start: Opening new page")
        self.page = await self.browser.new_page()
        print("b4 - on_start: Initializing PageManager")
        self.manager = PageManager(self.page)

    async def on_stop(self):
        print("c1 - on_stop: Stopping Playwright")
        if self.page:
            print("c2 - on_stop: Closing page")
            await self.page.close()
        if self.browser:
            print("c3 - on_stop: Closing browser")
            await self.browser.close()
        if self.playwright:
            print("c4 - on_stop: Stopping Playwright instance")
            await self.playwright.stop()

    def stop(self):
        print("d1 - stop: Attempting to cancel task")
        if self._task:
            self._task.cancel()
            try:
                print("d2 - stop: Awaiting task cancellation")
                asyncio.get_event_loop().run_until_complete(self._task)
            except asyncio.CancelledError:
                print("d3 - stop: Task was successfully cancelled")

    @task
    async def load_test_pizza(self):
        print("00 - load_test_pizza: Starting task")
        if not self.page:
            print("01 - load_test_pizza: Page is not initialized")
            return
        print("02 - load_test_pizza: Navigating to page")
        await self.page.goto("https://app.magna.isa.gov.il/")
        print("03 - load_test_pizza: Checking PageManager and MainPage")
        if not self.manager or not self.manager.main_page:
            print("04 - load_test_pizza: PageManager or MainPage is not initialized")
            raise Exception("PageManager or MainPage is not initialized properly")
        print("05 - load_test_pizza: Performing search")
        await self.manager.main_page.search("520000118")
        for i in range(20):
            print(f"06 - load_test_pizza: Clicking report result {i+1}/20")
            await self.manager.main_page.result_table.click_nth_report_result(0)
            print(f"07 - load_test_pizza: Going back after click {i+1}/20")
            await self.manager.main_page.back()

    def run(self):
        print("a1 - run: Getting event loop")
        try:
            loop = asyncio.get_event_loop()
            print("a2 - run: Event loop retrieved")
        except RuntimeError as e:
            print("a3 - run: No event loop found, creating new one")
            if str(e).startswith('There is no current event loop in thread'):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                print("a4 - run: New event loop created and set")
        print("a5 - run: Scheduling _run task")
        self._task = loop.create_task(self._run())  # Schedule the task on the event loop
        print("a6 - run: Starting event loop")
        loop.run_forever()  # Ensure the loop runs to keep the task active

    async def _run(self):
        print("b1 - _run: Starting _run coroutine")
        await self.on_start()
        try:
            while True:
                print("b2 - _run: Entering main loop")
                await self.load_test_pizza()
                print("b3 - _run: Sleeping between tasks")
                await asyncio.sleep(self.wait_time())
        finally:
            print("b4 - _run: Cleaning up before exit")
            await self.on_stop()
