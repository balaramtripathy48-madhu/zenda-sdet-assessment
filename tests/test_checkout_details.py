import logging
import os

from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_logged_in_user_checkout_details(page: Page):
    logger.info("TEST START: Logged-in user checkout details")

    # Step 1: Open the website
    logger.info("STEP 1: Navigate to the website homepage")
    page.goto(page.base_url)

    # Step 2: Initialize LoginPage
    logger.info("STEP 2: Initialize LoginPage")
    login_page = LoginPage(page)

    # Step 3: Open the login page
    logger.info("STEP 3: Open the login page")
    login_page.open_login_page()

    # Step 4: Login using credentials from .env
    logger.info("STEP 4: Login using test account credentials from .env")
    login_page.login(
        email=os.getenv("TEST_EMAIL"),
        password=os.getenv("TEST_PASSWORD")
    )

    # Step 5: Verify login succeeded
    logger.info("STEP 5: Verify login was successful")
    expect(
        page.get_by_text("Logged in as", exact=False)
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Logged-in user indicator is visible")

    # Step 6: Initialize CartPage
    logger.info("STEP 6: Initialize CartPage")
    cart_page = CartPage(page)

    # Step 7: Add the first product to the cart
    logger.info("STEP 7: Add the first product to the cart")
    cart_page.add_first_product_to_cart()

    # Step 8: Verify product-added confirmation popup
    logger.info("STEP 8: Verify product-added confirmation popup")
    expect(
        page.get_by_text(
            "Your product has been added to cart",
            exact=False
        )
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Product-added confirmation popup is visible")

    # Step 9: Open the cart using the popup
    logger.info("STEP 9: Open cart using View Cart button")
    page.get_by_role("link", name="View Cart").click()

    # Step 10: Verify cart page is visible
    logger.info("STEP 10: Verify cart page is visible")
    expect(page).to_have_url(
        "https://automationexercise.com/view_cart"
    )
    logger.info("ASSERTION PASSED: Cart page is visible")

    # Step 11: Verify checkout is available
    logger.info("STEP 11: Verify Proceed To Checkout button is visible")
    expect(
        page.get_by_text("Proceed To Checkout", exact=False)
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Proceed To Checkout is visible")

    # Step 12: Proceed to checkout
    logger.info("STEP 12: Proceed to checkout")
    cart_page.proceed_to_checkout()

    # Step 13: Verify Address Details section
    logger.info("STEP 13: Verify Address Details section is visible")
    expect(
        page.get_by_text("Address Details", exact=False)
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Address Details section is visible")

    # Step 14: Verify Review Your Order section
    logger.info("STEP 14: Verify Review Your Order section is visible")
    expect(
        page.get_by_text("Review Your Order", exact=False)
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Review Your Order section is visible")

    logger.info("TEST PASSED: Logged-in user checkout details")