import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_recordandplay(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").fill("Learning@830$3mK2")
    page.locator("span").nth(4).click()
    page.get_by_role("radio", name="User").check()
    page.get_by_role("button", name="Okay").click()
    page.get_by_role("combobox").select_option("teach")
    page.locator("span").nth(2).click()
    page.get_by_role("radio", name="Admin").check()
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    page.locator("app-card").filter(has_text="iphone X $24.99 Lorem ipsum").get_by_role("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge $24.99 Lorem ipsum").get_by_role("button").click()
    page.get_by_text("Checkout ( 2 ) (current)").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Purchase").click()

    # ---------------------
    context.close()
    browser.close()
