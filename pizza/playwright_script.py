from playwright.sync_api import sync_playwright

def browse_pizza_website():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://app.magna.isa.gov.il/")
        # Add more interactions here if needed
        browser.close()
