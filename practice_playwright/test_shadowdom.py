from playwright.sync_api import Playwright


def test_shadowdom(playwright:Playwright):
    browser =playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()

    page.goto("https://www.lambdatest.com/selenium-playground/shadow-dom")
    page.locator("div", has_text="Name").fill("Komal")