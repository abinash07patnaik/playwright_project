from playwright.sync_api import Page, expect, Playwright
from utils.api_base import APIUtils

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6ae31044a90a419aa8326417")


def test_network_2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("patnaikabinash07@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abichinu@#12345")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")

def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    token= api_utils.getToken(playwright)

    driver = playwright.chromium.launch(headless=False)
    context = driver.new_context()
    page = context.new_page()

    #script to inject token in session to bypass login
    page.add_init_script(f"""
                        localStorage.setItem('token','{token}')
                        """)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
