from playwright.sync_api import Page, expect


def test_tables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #Get the Price value of Rice
    #get the column of price
    #get the rice row
    #extract the price for rice

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            pricecolvalue = index
            print(f"Price value {pricecolvalue}")
            break;

    ricerow = page.locator("tr").filter(has_text="Rice")
    expect(ricerow.locator("td").nth(pricecolvalue)).to_contain_text("37")



