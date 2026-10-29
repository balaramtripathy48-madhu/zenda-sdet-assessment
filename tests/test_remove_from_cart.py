import logging

from playwright.sync_api import Page, expect
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


def test_remove_product_from_cart(page: Page):
    logger.info("TEST START: Remove product from cart")

    # Step 1: Open the website
    logger.info("STEP 1: Navigate to the Automation Exercise homepage")
    page.goto("https://automationexercise.com/")

    # Step 2: Add a product to the cart
    logger.info("STEP 2: Locate the first product")
    product = page.locator(".product-image-wrapper").first

    logger.info("STEP 3: Hover over the first product")
    product.hover()

    logger.info("STEP 4: Click Add to Cart")
    product.locator(".add-to-cart").first.click()

    # Step 3: Verify product-added confirmation
    logger.info("STEP 5: Verify the product-added confirmation popup")
    expect(
        page.get_by_text("Your product has been added to cart")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Product-added confirmation popup is visible")

    # Step 4: Open the cart
    logger.info("STEP 6: Click View Cart")
    page.get_by_text("View Cart", exact=True).click()

    # Step 5: Initialize CartPage
    logger.info("STEP 7: Initialize CartPage")
    cart_page = CartPage(page)

    # Step 6: Verify the product is present
    logger.info("STEP 8: Verify the product is displayed in the cart")
    expect(cart_page.get_cart_products()).to_be_visible()
    logger.info("ASSERTION PASSED: Product is visible in the cart")

    # Step 7: Remove the product
    logger.info("STEP 9: Remove the product from the cart")
    cart_page.remove_product()

    # Step 8: Verify the cart is empty
    logger.info("STEP 10: Verify the cart is empty")
    expect(
        page.get_by_text("Cart is empty!", exact=False)
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Cart empty message is visible")

    logger.info("TEST PASSED: Remove product from cart")