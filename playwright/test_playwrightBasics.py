import time

import pytest
from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_Corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role(role="combobox").select_option("teach")
    page.get_by_role(role="link", name="terms and conditions").click()
    # page.get_by_role(role="checkbox").click()
    page.locator("#terms").check()
    page.get_by_role(role="button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    time.sleep(10)

