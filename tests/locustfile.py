import asyncio
import sys
import os
import asyncio
import threading
import concurrent.futures

from playwright.async_api import async_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locust import HttpUser, TaskSet, task
from pages.page_manager import PageManager


class MainPageLoadTest(TaskSet):
    def on_start(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.future = self.executor.submit(self.loop.run_until_complete, self.setup())

    async def setup(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.page = await self.browser.new_page()
        self.manager = PageManager(self.page)  # Initialize the manager here

    @task
    def test_main_page(self):
        future = asyncio.run_coroutine_threadsafe(self.run_test(), self.loop)
        future.result()  # Wait for the coroutine to finish

    async def run_test(self):
        await self.manager.main_page.open()
        await self.manager.main_page.search("520000118")
        for _ in range(20):
            await self.manager.main_page.result_table.click_nth_report_result(0)
            await self.manager.main_page.back()

    def on_stop(self):
        self.loop.run_until_complete(self.teardown())
        self.loop.stop()
        self.executor.shutdown()

    async def teardown(self):
        await self.browser.close()
        await self.playwright.stop()

class WebsiteUser(HttpUser):
    tasks = [MainPageLoadTest]
    host = "https://app.magna.isa.gov.il/"
    min_wait = 1000
    max_wait = 2000