import json

import pytest
from playwright.sync_api import Playwright
from pathlib import Path
from pageObjects.login import LoginPage
from utils.api_baseframework import APIUtils

ROOT_DIR = Path(__file__).resolve().parent.parent
credentials_path = ROOT_DIR / "playwright" / "data" / "credentials.json"


with open(credentials_path) as f:
    data = json.load(f)
    user_credentials_list = data['user_credentials']


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_web_api(playwright:Playwright, browserInstance, user_credentials):

    user_email = user_credentials['user_email']
    user_password = user_credentials['user_password']

    #create order using API
    api_utils = APIUtils()
    order_response = api_utils.createOrder(playwright, user_email, user_password)
    order_id = order_response["orders"][0]

    #login
    login_page = LoginPage(browserInstance) # Creating login page class object
    login_page.navigate()
    dashboard_page = login_page.login(user_email, user_password)

    #go to orders history page and confirm order created
    order_history_page = dashboard_page.selectOrdersNavLink()
    order_detail_page = order_history_page.selectOrder(order_id)

    #validate in order details page
    order_detail_page.validate_order_details(order_id)

