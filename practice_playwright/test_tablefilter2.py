from playwright.sync_api import Playwright, expect


def test_tables(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context_info = browser.new_context()
    page = context_info.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground/table-search-filter-demo")

    #Get the Javascript Assignee
    #get the column of Assignee
    #get the Javascript row
    #extract the Javascript Assignee

    for index in range (page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Assignee").count()>0:
            assigneecolum = index
            print("the task colum" ,{assigneecolum})
            break


    taskrow = page.locator("tr").filter(has_text="JavaScript")
    expect(taskrow.locator("td").nth(assigneecolum)).to_contain_text("Dan Akaa")







