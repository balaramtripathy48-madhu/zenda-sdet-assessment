import logging

from playwright.sync_api import Page, expect
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


def test_checkout_without_login(page: Page):
    logger.info("TEST START: Checkout without login")

    # Step 1: Open the website
    logger.info("STEP 1: Navigate to the Automation Exercise homepage")
    page.goto("https://automationexercise.com/")

    # Step 2: Initialize CartPage
    logger.info("STEP 2: Initialize CartPage")
    cart_page = CartPage(page)

    # Step 3: Add a product to the cart
    logger.info("STEP 3: Add the first product to the cart")
    cart_page.add_first_product_to_cart()

    # Step 4: Verify product-added confirmation
    logger.info("STEP 4: Verify the product-added confirmation popup")
    expect(
        page.get_by_text("Your product has been added to cart")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Product-added confirmation popup is visible")

    # Step 5: Open cart
    logger.info("STEP 5: Open the cart from the confirmation popup")
    cart_page.view_cart_from_popup()

    # Step 6: Proceed to checkout
    logger.info("STEP 6: Proceed to checkout")
    cart_page.proceed_to_checkout()

    # Step 7: Verify guest is prompted to register or log in
    logger.info("STEP 7: Verify Register / Login prompt is displayed")
    expect(
        page.get_by_role("link", name="Register / Login")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Guest is prompted to register or log in")

    logger.info("TEST PASSED: Checkout without login")