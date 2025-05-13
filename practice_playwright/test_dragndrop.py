from playwright.sync_api import Playwright, expect


def test_dragndrop(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo")

    page.locator("#slider1").get_by_role("slider").fill("18")
    expect(page.get_by_text("18")).to_be_visible()

    context_info.close()
    browser.close()

