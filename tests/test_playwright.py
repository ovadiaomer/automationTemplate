from pages.page_manager import PageManager

def test_playwright(browser):
    manager = PageManager(browser)
    manager.main_page.open()
    manager.close()
