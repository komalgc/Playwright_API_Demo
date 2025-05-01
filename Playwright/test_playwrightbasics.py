import time


from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


def test_locatorsdemo(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    time.sleep(5)






def test_locatorsdemofailed(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learnineg")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


def test_fiefoxbrowser(playwright: Playwright):
    firefoxbrowser = playwright.firefox.launch(headless=False)
    page = firefoxbrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)


