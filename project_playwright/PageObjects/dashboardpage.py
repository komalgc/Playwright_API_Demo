
from project_playwright.PageObjects.orderhistorypage import OrdersHistoryPage


class DashboardPage:


    def __init__(self, page):
        self.page = page

    def  selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderhistory = OrdersHistoryPage(self.page)
        return orderhistory