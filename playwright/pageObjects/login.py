from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.email_box = self.page.get_by_placeholder("email@example.com")
        self.password_box = self.page.get_by_placeholder("enter your passsword")
        self.login_button = self.page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")


    def login(self, user_email, user_password):
        self.email_box.fill(user_email)
        self.password_box.fill(user_password)
        self.login_button.click()
        dashboard_page = DashboardPage(page=self.page)
        return dashboard_page