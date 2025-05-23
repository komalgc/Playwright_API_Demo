from playwright.sync_api import Playwright, expect


def test_bootstrapduallist(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/bootstrap-dual-list-box-demo")
    page.get_by_placeholder("search").nth(0).fill("Danville")
    page.locator(".list-group-item").filter(has_text="Danville").click()
    page.locator(".list-arrows").filter(has=page.get_by_role("button", name= " >")).click()
    expect(page.locator(".well").filter(has=page.locator(".list-group-item")).filter(has_text="Danville")).to_be_visible()

