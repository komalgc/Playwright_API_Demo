from playwright.sync_api import Playwright


def test_alert(playwright:Playwright):
    browser =playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()

    page.goto("https://www.lambdatest.com/selenium-playground/context-menu")
    page.locator("#hot-spot").click(button="right")

    # Register dialog handler
    def handle_dialog(dialog):
        print("Alert Text:", dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    # Set up dialog (alert) handler
  #  page.once("dialog", lambda dialog: (print("Alert Text:", dialog.message),dialog.accept()))



    #page.once("dialog", lambda dialog: dialog.dismiss())