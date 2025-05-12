from playwright.sync_api import Page, expect


def test_uivalidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name= "terms and conditions").click()
    page.get_by_role("button", name= "Sign In").click()
    iphoneproduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneproduct.get_by_role("button").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Blackberry")
    nokiaproduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

