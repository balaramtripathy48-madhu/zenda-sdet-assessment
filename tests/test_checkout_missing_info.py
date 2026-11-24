import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, then

logger = logging.getLogger(__name__)

scenarios("../features/checkout_missing_info.feature")


@then('the "Place Order" link should be visible')
def place_order_visible(page: Page):
    logger.info("ASSERTION: Verify Place Order link is visible")
    expect(page.get_by_role("link", name="Place Order")).to_be_visible()
