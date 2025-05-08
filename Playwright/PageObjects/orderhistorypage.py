from Playwright.PageObjects.orderdetailspage import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self,page):
        self.page = page


    def viewOrders(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)
        row.get_by_role("button", name="View").click()
        orderdetailspage = OrderDetailsPage(self.page)
        return orderdetailspage


