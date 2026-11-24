import logging
import os

from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_checkout_navigation_back_to_cart(page: Page):
    logger.info("TEST START: Checkout navigation back to cart")

    # Step 1: Open website
    logger.info("STEP 1: Navigate to the website homepage")
    page.goto(page.base_url)

    # Step 2: Open login page
    logger.info("STEP 2: Initialize LoginPage")
    login_page = LoginPage(page)

    logger.info("STEP 3: Open the login page")
    login_page.open_login_page()

    # Step 3: Login using test account from .env
    logger.info("STEP 4: Login using test account credentials from .env")
    login_page.login(
        email=os.getenv("TEST_EMAIL"),
        password=os.getenv("TEST_PASSWORD")
    )

    # Step 4: Verify login succeeded
    logger.info("STEP 5: Verify successful login")
    expect(
        page.get_by_text("Logged in as", exact=False)
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Logged-in user indicator is visible")

    # Step 5: Add product
    logger.info("STEP 6: Initialize CartPage")
    cart_page = CartPage(page)

    logger.info("STEP 7: Add the first product to the cart")
    cart_page.add_first_product_to_cart()

    # Step 6: Verify product-added confirmation
    logger.info("STEP 8: Verify product-added confirmation popup")
    expect(
        page.get_by_text("Your product has been added to cart")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Product-added confirmation popup is visible")

    # Step 7: Open cart and checkout
    logger.info("STEP 9: Open the cart from the confirmation popup")
    cart_page.view_cart_from_popup()

    logger.info("STEP 10: Proceed to checkout")
    cart_page.proceed_to_checkout()

    # Step 8: Verify checkout page
    logger.info("STEP 11: Verify Address Details section is visible")
    expect(page.get_by_text("Address Details")).to_be_visible()
    logger.info("ASSERTION PASSED: Address Details section is visible")

    # Step 9: Navigate back to cart
    logger.info("STEP 12: Navigate back to the previous page")
    page.go_back()

    # Step 10: Verify cart page is displayed
    logger.info("STEP 13: Verify the browser returned to the cart page")
    expect(page).to_have_url("https://automationexercise.com/view_cart")
    logger.info("ASSERTION PASSED: Cart page URL is displayed")

    logger.info("STEP 14: Verify cart products are visible")
    expect(cart_page.get_cart_products()).to_be_visible()
    logger.info("ASSERTION PASSED: Cart products are visible")

    logger.info("TEST PASSED: Checkout navigation back to cart")