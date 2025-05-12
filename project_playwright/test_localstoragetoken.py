from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from utils.apibase import APIBase


def test_localstoragetoken(playwright:Playwright):

    api_utils=APIBase()
    getToken=api_utils.gettoken(playwright)


    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #getthe token for bypassing loginn
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()