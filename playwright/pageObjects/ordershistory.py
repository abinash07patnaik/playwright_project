from .orderdetail import OrderDetailPage

class OrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, order_id):
        row = self.page.locator("tr").filter(has_text=order_id)
        row.get_by_role("button", name="View").click()
        order_detail_page = OrderDetailPage(self.page)
        return order_detail_page

