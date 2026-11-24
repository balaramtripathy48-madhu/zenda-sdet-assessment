import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, then

logger = logging.getLogger(__name__)

scenarios("../features/checkout_guest.feature")


@then('the user is prompted with "Register / Login"')
def guest_prompted_register_or_login(page: Page):
    logger.info("ASSERTION: Verify Register / Login prompt is displayed")
    expect(page.get_by_role("link", name="Register / Login")).to_be_visible()
