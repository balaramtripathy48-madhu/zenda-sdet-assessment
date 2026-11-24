import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)

scenarios("../features/update_cart_quantity.feature")


@given(parsers.parse('the user navigates to product details for product "{product_id}"'))
def navigate_to_product_details(page: Page, product_id: str):
    logger.info("ACTION: Navigate to product details for id: %s", product_id)
    page.goto(f"https://automationexercise.com/product_details/{product_id}")
    expect(page.locator("#quantity")).to_be_visible()


@when(parsers.parse('the user sets the product quantity to "{quantity}"'))
def set_product_quantity(page: Page, quantity: str):
    logger.info("ACTION: Set quantity to %s", quantity)
    page.locator("#quantity").fill(quantity)


@when("the user clicks Add to Cart on product details")
def click_add_to_cart_details(page: Page):
    logger.info("ACTION: Click Add to Cart button on details page")
    page.get_by_role("button", name="Add to cart").click()


@then(parsers.parse('the cart quantity should be "{expected_quantity}"'))
def verify_cart_quantity(page: Page, expected_quantity: str):
    logger.info("ASSERTION: Cart quantity should be %s", expected_quantity)
    cart_page = CartPage(page)
    expect(cart_page.get_cart_quantity()).to_have_text(expected_quantity)
