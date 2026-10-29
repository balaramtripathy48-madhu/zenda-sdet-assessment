import logging

from playwright.sync_api import Page, expect
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


def test_add_product_to_cart(page: Page):
    logger.info("TEST START: Add product to cart")

    # Step 1: Open the website
    logger.info("STEP 1: Navigate to the Automation Exercise homepage")
    page.goto("https://automationexercise.com/")

    # Step 2: Initialize CartPage
    logger.info("STEP 2: Initialize CartPage")
    cart_page = CartPage(page)

    # Step 3: Add a product to the cart
    logger.info("STEP 3: Add the first product to the cart")
    cart_page.add_first_product_to_cart()

    # Step 4: Verify the confirmation popup
    logger.info("STEP 4: Verify the product-added confirmation popup")
    expect(
        page.get_by_text("Your product has been added to cart")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Product-added confirmation popup is visible")

    # Step 5: Open the cart
    logger.info("STEP 5: Open the cart from the confirmation popup")
    cart_page.view_cart_from_popup()

    # Step 6: Verify the product appears in the cart
    logger.info("STEP 6: Verify the product is displayed in the cart")
    expect(cart_page.get_cart_products()).to_be_visible()
    logger.info("ASSERTION PASSED: Product is visible in the cart")

    logger.info("TEST PASSED: Add product to cart")