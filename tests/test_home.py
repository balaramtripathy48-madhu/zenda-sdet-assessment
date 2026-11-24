import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, then

logger = logging.getLogger(__name__)

scenarios("../features/home.feature")


@given("the user navigates to the homepage")
def navigate_to_homepage(page: Page):
    logger.info("ACTION: Navigate to homepage")
    page.goto(page.base_url)


@then('the page title should be "Automation Exercise"')
def verify_page_title(page: Page):
    logger.info("ASSERTION: Verify page title")
    expect(page).to_have_title("Automation Exercise")
