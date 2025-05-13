from playwright.sync_api import Playwright, expect


def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/checkbox-demo")
    page.locator("#isAgeSelected").check()
    expect(page.locator("#isAgeSelected")).to_be_checked()