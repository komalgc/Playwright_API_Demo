import json

import pytest
from playwright.sync_api import Playwright, expect

from Playwright.PageObjects.dashboardpage import DashboardPage
from Playwright.PageObjects.loginpage import LoginPage
from utils.apibase import APIBase

# Json-->util-->access to test
with open('data/credentials.json') as f:
    testdata = json.load(f)
    print(testdata)
    user_credential_list = testdata['user_credentials']

@pytest.mark.parametrize('user_credentials',user_credential_list)
def test_webapi(playwright:Playwright, user_credentials):
    useremail = user_credentials["userEmail"]
    userpassword = user_credentials["userPassword"]


    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #create order  -> orderId
    apiutils = APIBase()
    orderId= apiutils.createorder(playwright, user_credentials)


    #loginpage
    loginPage =LoginPage(page)
    loginPage.navigate()
    loginPage.login(useremail,userpassword)

    #dashboardpage
    dashboard = DashboardPage(page)
    dashboard.selectOrdersNavLink()

    #orders history page -> order is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")