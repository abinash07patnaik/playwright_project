from playwright.sync_api import expect


class OrderDetailPage:

    def __init__(self, page):
        self.page = page

    def validate_order_details(self, order_id):
        expect(self.page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
        expect(self.page.get_by_text(f"{order_id}")).to_be_visible()
