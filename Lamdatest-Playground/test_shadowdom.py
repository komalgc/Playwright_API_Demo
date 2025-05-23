from playwright.sync_api import Playwright, expect


def test_shadowdom(playwright:Playwright):
    browser =playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()

    page.goto("https://www.lambdatest.com/selenium-playground/shadow-dom")

    page.locator("#shadow_host").shadow_root().get_by
    expect(page.locator("div >> shadow=button").filter(has_text="Shadow DOM example")).to_contain_text("Shadow DOM example")

