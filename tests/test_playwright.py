from pages.page_manager import PageManager

def test_playwright(browser):
    manager = PageManager(browser)
    manager.playwright_page.open()
    manager.playwright_page.get_started_button.click()
    assert manager.page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"
    manager.close()
