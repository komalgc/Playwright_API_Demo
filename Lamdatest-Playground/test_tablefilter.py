from playwright.sync_api import Playwright, Page, expect
from pytest_playwright.pytest_playwright import browser


def test_tablefilter(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context_info= browser.new_context()
    page= context_info.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/table-records-filter-demo")
    page.get_by_role("button", name="Selenium Testing").click()
    expect(page.locator(".summary").nth(1)).to_contain_text("Test on Selenium Grid Cloud of 3000")