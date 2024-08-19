from playwright.sync_api import Browser, Page

from models.company import Company
from pages.page_manager import PageManager
from locust import HttpUser, task


class LoadTest(HttpUser):
    @task
    def test_main_page(self):
        manager = PageManager(self.client)
        manager.main_page.open()
        metrics = self.client.evaluate("() => JSON.stringify(window.performance.timing)")
        manager.main_page.search(Company.BANK_HAPOALIM.value)
        for i in range(20):
            manager.main_page.result_table.click_nth_report_result(00)
            manager.main_page.back()
