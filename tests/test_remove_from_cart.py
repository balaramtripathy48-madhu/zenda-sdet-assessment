import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, when, then
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)

scenarios("../features/remove_from_cart.feature")


@when("the user removes the product from the cart")
def remove_product(page: Page):
    logger.info("ACTION: Remove product from cart")
    cart_page = CartPage(page)
    cart_page.remove_product()


@then('the message "Cart is empty!" should be visible')
def cart_is_empty(page: Page):
    logger.info("ASSERTION: Cart is empty message is visible")
    expect(page.get_by_text("Cart is empty!", exact=False)).to_be_visible()
