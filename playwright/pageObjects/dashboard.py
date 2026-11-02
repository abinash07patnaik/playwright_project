from .ordershistory import OrderHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page
        self.orders_button = self.page.get_by_role("button", name="ORDERS")

    def selectOrdersNavLink(self):
        self.orders_button.click()
        orders_history_page = OrderHistoryPage(self.page)
        return orders_history_page