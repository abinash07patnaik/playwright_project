import time

from playwright.sync_api import Page, expect, Playwright


def test_UIChecks(page:Page):
    #hide/display placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #alert boxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    #mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    #frame handling
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link",name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

    #check price of rice =37
    #identify price column
    #identify rice row
    #extract price of rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            pricecolVal = index
            print(f"Price col val is {pricecolVal}")
            break
    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(pricecolVal)).to_contain_text("37")




    time.sleep(5)




