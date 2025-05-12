import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import json

import pytest
from playwright.sync_api import Playwright

from project_playwright.PageObjects import dashboardpage
from project_playwright.PageObjects.dashboardpage import DashboardPage
from project_playwright.PageObjects.loginpage import LoginPage
from utils.apibase import APIBase

# Json-->util-->access to test
with open('data/credentials.json') as f:
    testdata = json.load(f)
    print(testdata)
    user_credential_list = testdata['user_credentials']

@pytest.mark.parametrize('user_credentials',user_credential_list)
def test_webapi(playwright:Playwright, browserInstance, user_credentials):
    useremail = user_credentials["userEmail"]
    userpassword = user_credentials["userPassword"]


    #create order  -> orderId
    apiutils = APIBase()
    orderId= apiutils.createorder(playwright, user_credentials)


    #loginpage
    loginPage =LoginPage(browserInstance)
    loginPage.navigate()
    dashboardpage = loginPage.login(useremail, userpassword)
    #dashboardpage

    orderhistory = dashboardpage.selectOrdersNavLink()
    orderdetailspage= orderhistory.viewOrders(orderId)

    #orders history page -> order is present
    orderdetailspage.orderdetails()

