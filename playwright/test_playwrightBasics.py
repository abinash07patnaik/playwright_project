import pytest
from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")
