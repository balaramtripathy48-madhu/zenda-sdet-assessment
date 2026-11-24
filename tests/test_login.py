import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)

scenarios("../features/login.feature")


@given("the user is on the login page")
def user_on_login_page(page: Page):
    logger.info("ACTION: Open login page")
    login_page = LoginPage(page)
    login_page.open_login_page()


@when("the user submits invalid login credentials")
def submit_invalid_login(page: Page):
    logger.info("ACTION: Enter invalid credentials and click login")
    login_page = LoginPage(page)
    login_page.login(
        email="invaliduser123@example.com",
        password="WrongPassword123"
    )


@then('an error message "Your email or password is incorrect!" should be visible')
def verify_invalid_login_error(page: Page):
    logger.info("ASSERTION: Verify invalid login error message")
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
