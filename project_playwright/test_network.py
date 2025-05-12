from playwright.sync_api import Playwright

fakepayloadresponse = {"data": [],"message": "No orders"}

def intercept_response(route):
    route.fulfill(
        json = fakepayloadresponse
    )

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
    order_text=page.locator(".mt-4").text_content()
    print(order_text)



