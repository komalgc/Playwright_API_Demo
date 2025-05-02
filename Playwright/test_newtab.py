from playwright.sync_api import Page


def test_newtabe(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage_info:
        #step1
        #step2
        page.locator(".blinkingText").click() #newpage
        childpage = newpage_info.value
        text = childpage.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"