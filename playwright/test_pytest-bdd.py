import pytest
import pytest_bdd
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from utils.api_baseframework import APIUtils
from pageObjects.login import LoginPage

scenarios('features/ordertransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("place the item order with {username} and {password}"))
def place_item_order(playwright:Playwright, username, password, shared_data):
    api_utils = APIUtils()
    order_response = api_utils.createOrder(playwright, username, password)
    order_id = order_response["orders"][0]
    shared_data["order_id"] = order_id

@given("user is on landing page")
def user_on_landing_page(browserInstance, shared_data):
    login_page = LoginPage(browserInstance)  # Creating login page class object
    login_page.navigate()
    shared_data['login_page'] = login_page

@when(parsers.parse("I login to portal with {username} and {password}"))
def login_to_portal(username,password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data["dashboard_page"] = dashboard_page

@when("navigate to orders page")
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data["dashboard_page"]
    order_history_page = dashboard_page.selectOrdersNavLink()
    shared_data["order_history_page"]= order_history_page

@when("select the orderId")
def select_orderid(shared_data):
    order_history_page = shared_data["order_history_page"]
    order_id = shared_data["order_id"]
    order_detail_page = order_history_page.selectOrder(order_id)
    shared_data["order_detail_page"] = order_detail_page

@then("order message is successfully displayed")
def message_displayed(shared_data):
    order_detail_page = shared_data["order_detail_page"]
    order_id = shared_data["order_id"]
    order_detail_page.validate_order_details(order_id)


