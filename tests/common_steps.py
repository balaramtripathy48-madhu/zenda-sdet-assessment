import logging
import os
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.config_reader import get_base_url

logger = logging.getLogger(__name__)


@given("the user navigates to the homepage")
@given("the user is on the homepage")
def navigate_to_homepage(page: Page):
    logger.info("ACTION: Navigate to homepage")
    page.goto(page.base_url)


@given("the user is logged in with test credentials")
def logged_in_user(page: Page):
    logger.info("ACTION: Login with test credentials")
    page.goto(page.base_url)
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(
        email=os.getenv("TEST_EMAIL"),
        password=os.getenv("TEST_PASSWORD")
    )
    expect(page.get_by_text("Logged in as", exact=False)).to_be_visible()
    logger.info("ASSERTION: Logged in successfully")


@when("the user adds the first product to the cart")
def add_first_product(page: Page):
    logger.info("ACTION: Add first product to cart")
    cart_page = CartPage(page)
    cart_page.add_first_product_to_cart()


@then("the product-added confirmation popup should be visible")
def popup_visible(page: Page):
    logger.info("ASSERTION: Product-added confirmation popup is visible")
    expect(page.get_by_text("Your product has been added to cart", exact=False)).to_be_visible()


@when("the user opens the cart from the popup")
def open_cart_from_popup(page: Page):
    logger.info("ACTION: Open cart from popup")
    cart_page = CartPage(page)
    cart_page.view_cart_from_popup()


@then("the product should be displayed in the cart")
def product_in_cart(page: Page):
    logger.info("ASSERTION: Product is visible in cart")
    cart_page = CartPage(page)
    expect(cart_page.get_cart_products()).to_be_visible()


@when("the user proceeds to checkout")
def proceed_to_checkout(page: Page):
    logger.info("ACTION: Proceed to checkout")
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()


@then('the "Address Details" section should be visible')
def address_details_visible(page: Page):
    logger.info("ASSERTION: Address Details section is visible")
    expect(page.get_by_text("Address Details", exact=False)).to_be_visible()


@then('the "Review Your Order" section should be visible')
def review_order_visible(page: Page):
    logger.info("ASSERTION: Review Your Order section is visible")
    expect(page.get_by_text("Review Your Order", exact=False)).to_be_visible()
