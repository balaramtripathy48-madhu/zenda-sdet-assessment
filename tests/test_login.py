import logging

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_invalid_login(page: Page):
    logger.info("TEST START: Invalid login")

    # Step 1: Initialize LoginPage
    logger.info("STEP 1: Initialize LoginPage")
    login_page = LoginPage(page)

    # Step 2: Open login page
    logger.info("STEP 2: Open the login page")
    login_page.open_login_page()

    # Step 3: Enter invalid credentials and attempt login
    logger.info("STEP 3: Attempt login using invalid credentials")
    login_page.login(
        email="invaliduser123@example.com",
        password="WrongPassword123"
    )

    # Step 4: Verify the error message
    logger.info("STEP 4: Verify the invalid-login error message is displayed")
    expect(
        page.get_by_text("Your email or password is incorrect!")
    ).to_be_visible()
    logger.info("ASSERTION PASSED: Invalid-login error message is visible")

    logger.info("TEST PASSED: Invalid login")