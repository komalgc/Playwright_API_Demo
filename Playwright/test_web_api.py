from playwright.sync_api import Playwright


def test_webapi(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()


    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahul.m.lokurte@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Wipro@123")
    page.get_by_role("button", name="Login").click()