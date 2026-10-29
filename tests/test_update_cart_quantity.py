import logging

from playwright.sync_api import Page, expect
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


def test_update_cart_quantity(page: Page):
    logger.info("TEST START: Update cart quantity")

    # Step 1: Open the first product details page directly
    logger.info("STEP 1: Navigate to the first product details page")
    page.goto("https://automationexercise.com/product_details/1")

    # Step 2: Verify product details page opened
    logger.info("STEP 2: Verify the product quantity field is visible")
    expect(page.locator("#quantity")).to_be_visible()
    logger.info("ASSERTION PASSED: Product quantity field is visible")

    # Step 3: Set quantity to 2
    logger.info("STEP 3: Set product quantity to 2")
    page.locator("#quantity").fill("2")

    # Step 4: Add product to cart
    logger.info("STEP 4: Click Add to Cart button")
    page.get_by_role("button", name="Add to cart").click()

    # Step 5: Verify confirmation
    logger.info("STEP 5: Verify the product-added confirmation popup")
    expect(
        page.get_by_text("Your product has been added to cart")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Product-added confirmation popup is visible")

    # Step 6: Open cart
    logger.info("STEP 6: Initialize CartPage")
    cart_page = CartPage(page)

    logger.info("STEP 7: Open the cart from the confirmation popup")
    cart_page.view_cart_from_popup()

    # Step 7: Verify quantity is 2
    logger.info("STEP 8: Verify the cart quantity is 2")
    expect(cart_page.get_cart_quantity()).to_have_text("2")
    logger.info("ASSERTION PASSED: Cart quantity is 2")

    logger.info("TEST PASSED: Update cart quantity")