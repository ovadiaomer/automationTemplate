from playwright.sync_api import Page

from components.button import Button
from components.locator import Locator
from components.text_input import TextInput
from config.config import Config
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.loader_circle = Locator(".mdc-circular-progress__spinner-layer", page)
        self.search_section = self.SearchSection(page, self)
        self.menu = self.Menu(page, self)
        self.result_table = self.ResultTable(page, self)
        self.wait_for_locator = self.result_table.report_list_single
        self.filter_section = self.FilterSection(page, self)

    def open(self):
        super().open(Config.BASE_URL)

    async def search(self, query):
        await self.search_section.perform_search(query)

    async def back(self):
        await self._page.go_back()
        await self.loader_circle.wait_for(state="hidden")

    class SearchSection:
        def __init__(self, page: Page, parent: 'MainPage'):
            self.page = page
            self.parent = parent
            self.search_container = Locator(".search-form", self.page)
            self.search_input = TextInput(".input-container input", self.page)
            self.search_company_dropdown = Locator(f'{self.search_container.selector} .company-dropdown', self.page)
            self.search_company_dropdown_items = Button(f'{self.search_company_dropdown.selector} .item', self.page)
            self.search_free_text = TextInput(".free-txt input", self.page)
            self.search_form = Locator('forms-selection', self.page)
            self.search_button = Button(f'{self.search_container.selector} button[title="חיפוש"]', self.page)
            self.search_filter_corporations = Button('div[title=" תאגידים ונאמני אג"ח "]', self.page)
            self.search_filter_mutual_funds = Button('div[title=" קרנות נאמנות ונאמנים "]', self.page)
            self.search_filter_portfolio_managers = Button('div[title=" מנהלי תיקים, יועצים ואנליסטים "]', self.page)
            self.search_filter_underwriters = Button('div[title=" חברות חיתום "]', self.page)
            self.search_filter_trading_arenas = Button('div[title=" זירות סוחר "]', self.page)
            self.search_filter_rating_companies = Button('div[title=" חברות דירוג "]', self.page)
            self.search_filter_offer_coordinator = Button('div[title=" רכז הצעה "]', self.page)
            self.search_filter_foreign_funds = Button('div[title=" קרנות זרות "]', self.page)

        async def perform_search(self, query: str):
            await self.search_input.fill(query)
            await self.search_company_dropdown_items.click()
            await self.search_button.click()
            await self.parent.loader_circle.wait_for(state="hidden")

    class Menu:
        def __init__(self, page: Page, parent: 'MainPage'):
            self.page = page
            self.parent = parent
            self.queries = Button("button[data-menu='queries)]", self.page)
            self.authority = Button("button[data-menu='authority)]", self.page)
            self.authority_submenu_news = Button("a[title='מעבר לאתר חיצוני']", self.page)
            self.authority_submenu_updates = Button("a[title='הודעות ועדכונים']", self.page)
            self.queries_submenu_corps = Button("button[title='תאגידים']", self.page)
            self.queries_submenu_mutual_funds = Button("button[title='קרנות נאמנות']", self.page)
            self.queries_submenu_company_by_type = Button("button[title='רשימת חברות לפי סוג']", self.page)

    class ResultTable:
        def __init__(self, page: Page, parent: 'MainPage'):
            self.page = page
            self.parent = parent
            self.table = Locator('.content', self.page)
            self.report_list_single = Locator(f'{self.table.selector} .report-list-single', self.page)
            self.table_rows = page.locator('table#results tbody tr')  # Adjust the selector

        def get_results(self):
            return self.report_list_single.get_locator().all()

        async def click_nth_report_result(self, nth: int = 0):
            results = await self.get_results()
            await results[nth].click()
            await self.parent.loader_circle.wait_for(state="hidden")

        async def get_nth_report_result_text_content(self, nth: int = 00):
            return await self.get_results()[nth].all_text_contents()

    class FilterSection:
        def __init__(self, page: Page, parent: 'MainPage'):
            self.page = page
            self.parent = parent
            self.filter_dropdown = page.locator('#filter-dropdown')  # Adjust the selector
            self.apply_filter_button = page.locator('#apply-filter')  # Adjust the selector

        def apply_filter(self, filter_value: str):
            self.filter_dropdown.select_option(filter_value)
            self.apply_filter_button.click()
