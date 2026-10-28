import time

from playwright.sync_api import Page, expect


def test_uiValidationDynamicScript(page: Page):
    # I want to select Nokia Edge and iPhone X into cart and verify 2 items are shown in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role(role="combobox").select_option("teach")
    page.get_by_role(role="link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role(role="button", name="Sign In").click()
    iphone_x_locator = page.locator("app-card").filter(has_text="iphone X")
    iphone_x_locator.get_by_role(role="button").click()
    nokia_edge_locator = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge_locator.get_by_role(role="button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.get_by_text("Nokia Edge")).to_be_visible()
    expect(page.get_by_text("iphone X")).to_be_visible()

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as child:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_page = child.value
        text_ = child_page.locator(".red").text_content()
        email_id = text_.split("at")[1].strip().split()[0]
        print(email_id)
        assert email_id == "mentor@rahulshettyacademy.com"
    time.sleep(5)