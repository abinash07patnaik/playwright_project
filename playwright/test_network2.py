from playwright.sync_api import Page, expect, Playwright

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6ae31044a90a419aa8326417")


def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("patnaikabinash07@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abichinu@#12345")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")
