from playwright.sync_api import Playwright, expect


def test_fileupload(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/upload-file-demo")
    page.locator("#file").click()
    page.set_input_files("input[type='file']", r"C:\Users\komal\Pictures\35eac1df-f692-4cba-95e9-bdc5c05b3a32.png")

    expect(page.get_by_text("File Successfully Uploaded")).to_be_visible()
