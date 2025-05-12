import time

from playwright.sync_api import Playwright

def intercept_request(route):
    route.continue_("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


def test_networkrequest(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahul.m.lokurte@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Wipro@123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    message= page.locator(".blink_me").text_content()
    print(message)
