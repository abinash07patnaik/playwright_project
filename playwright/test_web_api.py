from playwright.sync_api import Page, expect, Playwright

from utils.api_base import APIUtils

def test_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order using API
    api_utils = APIUtils()
    order_response = api_utils.createOrder(playwright)
    order_id = order_response["orders"][0]
    product_order_id = order_response["productOrderId"][0]
    message_order = order_response["message"]

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("patnaikabinash07@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abichinu@#12345")
    page.get_by_role("button", name="Login").click()

    #go to orders history page and confirm order created
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
    expect(page.get_by_text(f"{order_id}")).to_be_visible()

    context.close()

