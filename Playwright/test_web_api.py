from playwright.sync_api import Playwright, expect

from utils.apibase import APIBase


def test_webapi(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()


    #create order  -> orderId
    apiutils = APIBase()
    orderId= apiutils.createorder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahul.m.lokurte@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Wipro@123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #orders history page -> order is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")