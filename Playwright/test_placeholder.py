from playwright.sync_api import Page, expect


def test_placeholder(page:Page):

    #placeholder , Hide/show example

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name ="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #mousehove
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()


    #alerts

    page.on("dialog", lambda dialog:dialog.accept)
    page.get_by_role("button", name="Confirm").click()

    #framehandling

    pageframe=page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name ="All Access Plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers")