import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, then, parsers
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)

scenarios("../features/cart_quantity.feature")


@then(parsers.parse('the cart quantity should be "{expected_quantity}"'))
def verify_cart_quantity(page: Page, expected_quantity: str):
    logger.info("ASSERTION: Cart quantity should be %s", expected_quantity)
    cart_page = CartPage(page)
    expect(cart_page.get_cart_quantity()).to_have_text(expected_quantity)
