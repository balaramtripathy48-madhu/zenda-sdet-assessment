import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, when, then, parsers

logger = logging.getLogger(__name__)

scenarios("../features/checkout_navigation.feature")


@when("the user navigates back to the previous page")
def navigate_back(page: Page):
    logger.info("ACTION: Navigate back")
    page.go_back()


@then(parsers.parse('the cart page should be displayed with URL "{expected_url}"'))
def verify_cart_url(page: Page, expected_url: str):
    logger.info("ASSERTION: Verify cart URL is %s", expected_url)
    expect(page).to_have_url(expected_url)
