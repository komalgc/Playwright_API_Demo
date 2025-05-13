import pytest
from playwright.sync_api import Playwright

fakepayloadresponse = {"data": [],"message": "You have No Orders to show at this time.Please Visit Back Us"}

def intercept_response(route):
    route.fulfill(
        json = fakepayloadresponse
    )
@pytest.mark.smoke
def test_webapi(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    # login
    page.goto("https://rahulshettyacademy.com/client/")
    
    page.get_by_placeholder("email@example.com").fill("rahul.m.lokurte@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Wipro@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    #order_text=page.locator(".mt-4")
    order_text=page.wait_for_selector(".mt-4", timeout=60000).text_content()

    print(order_text)



