import json

import pytest
from playwright.sync_api import Page, expect, Playwright
from pathlib import Path
from utils.api_base import APIUtils


ROOT_DIR = Path(__file__).resolve().parent.parent
credentials_path = ROOT_DIR / "playwright" / "data" / "credentials.json"

with open(credentials_path) as f:
    data = json.load(f)
    user_credentials_list = data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_web_api(playwright:Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    user_email = user_credentials['user_email']
    user_password = user_credentials['user_password']

    #create order using API
    api_utils = APIUtils()
    order_response = api_utils.createOrder(playwright, user_email, user_password)
    order_id = order_response["orders"][0]

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_email)
    page.get_by_placeholder("enter your passsword").fill(user_password)
    page.get_by_role("button", name="Login").click()

    #go to orders history page and confirm order created
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
    expect(page.get_by_text(f"{order_id}")).to_be_visible()

    context.close()

