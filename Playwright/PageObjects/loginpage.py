from Playwright.PageObjects.dashboardpage import DashboardPage


class LoginPage:

    def __init__(self,page):
        self.page = page



    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")


    def login(self, username, password):
        self.page.get_by_placeholder("email@example.com").fill(username)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboardpage = DashboardPage(self.page)
        return dashboardpage

