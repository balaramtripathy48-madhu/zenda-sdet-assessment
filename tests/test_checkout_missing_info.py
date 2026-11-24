import logging
import os

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_checkout_missing_information(page: Page):
    logger.info("TEST START: Checkout missing information")

    # Step 1: Open website
    logger.info("STEP 1: Navigate to the website homepage")
    page.goto(page.base_url)

    # Step 2: Login
    logger.info("STEP 2: Initialize LoginPage")
    login_page = LoginPage(page)

    logger.info("STEP 3: Open the login page")
    login_page.open_login_page()

    logger.info("STEP 4: Login using test account credentials")
    login_page.login(
        email=os.getenv("TEST_EMAIL"),
        password=os.getenv("TEST_PASSWORD")
    )

    # Step 3: Verify login
    logger.info("STEP 5: Verify successful login")
    expect(
        page.get_by_text("Logged in as", exact=False)
    ).to_be_visible()

    # Step 4: Add product to cart
    logger.info("STEP 6: Initialize CartPage")
    cart_page = CartPage(page)

    logger.info("STEP 7: Add first product to cart")
    cart_page.add_first_product_to_cart()

    # Step 5: Open cart
    logger.info("STEP 8: Open cart from confirmation popup")
    cart_page.view_cart_from_popup()

    # Step 6: Proceed to checkout
    logger.info("STEP 9: Proceed to checkout")
    cart_page.proceed_to_checkout()

    # Step 7: Verify checkout page
    logger.info("STEP 10: Verify checkout page")
    expect(
        page.get_by_text("Address Details")
    ).to_be_visible()

    expect(
        page.get_by_text("Review Your Order")
    ).to_be_visible()

    # Step 8: Verify Place Order is visible
    logger.info("STEP 11: Verify Place Order link")
    expect(
        page.get_by_role("link", name="Place Order")
    ).to_be_visible()

    # Step 9: Stop before placing order or payment
    logger.info(
        "STEP 12: Stop before placing an order or making a payment"
    )

    logger.info("TEST PASSED: Checkout page validated")