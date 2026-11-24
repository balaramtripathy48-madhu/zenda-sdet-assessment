import logging

from playwright.sync_api import Page, expect

from pages.signup_page import SignupPage

from test_data.signup_data import (
    SIGNUP_NAME,
    SIGNUP_PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    ADDRESS,
    COUNTRY,
    STATE,
    CITY,
    ZIPCODE,
    MOBILE,
    generate_unique_email,
)

logger = logging.getLogger(__name__)


def test_signup_page_loads(page: Page):
    logger.info("TEST START: Verify signup page loads")

    # Step 1: Navigate to homepage
    logger.info("STEP 1: Navigate to the Automation Exercise homepage")
    page.goto("https://automationexercise.com/")

    # Step 2: Open Signup / Login page
    logger.info("STEP 2: Click Signup / Login link")
    page.get_by_role("link", name="Signup / Login").click()

    # Step 3: Verify signup page
    logger.info("STEP 3: Verify New User Signup heading is visible")
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    logger.info("ASSERTION PASSED: New User Signup heading is visible")
    logger.info("TEST PASSED: Verify signup page loads")


def test_signup_form(page: Page):
    logger.info("TEST START: Verify signup form submission")

    # Step 1: Navigate to homepage
    logger.info("STEP 1: Navigate to the Automation Exercise homepage")
    page.goto("https://automationexercise.com/")

    # Step 2: Open Signup / Login page
    logger.info("STEP 2: Click Signup / Login link")
    page.get_by_role("link", name="Signup / Login").click()

    # Step 3: Enter name
    logger.info("STEP 3: Enter signup name")
    page.get_by_placeholder("Name").fill(SIGNUP_NAME)

    # Step 4: Enter unique email
    logger.info("STEP 4: Enter signup email")
    page.locator(
        'form[action="/signup"] input[type="email"]'
    ).fill(generate_unique_email())

    # Step 5: Click Signup
    logger.info("STEP 5: Click Signup button")
    page.get_by_role("button", name="Signup").click()

    # Step 6: Verify next page
    logger.info("STEP 6: Verify Enter Account Information page is visible")
    expect(
        page.get_by_text("Enter Account Information")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Enter Account Information page is visible")
    logger.info("TEST PASSED: Verify signup form submission")


def test_create_new_account(page: Page):
    logger.info("TEST START: Create a new user account")

    # Create Signup Page Object
    signup_page = SignupPage(page)

    # Step 1: Open signup page
    logger.info("STEP 1: Open signup page")
    signup_page.open_signup_page()

    # Step 2: Enter signup name and unique email
    logger.info("STEP 2: Enter signup details")
    signup_page.enter_signup_details(
        SIGNUP_NAME,
        generate_unique_email(),
    )

    # Step 3: Verify account information page
    logger.info("STEP 3: Verify account information page")
    signup_page.verify_account_information_page()

    # Step 4: Fill account information and create account
    logger.info("STEP 4: Fill account information and create account")
    signup_page.fill_account_information(
        password=SIGNUP_PASSWORD,
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        address=ADDRESS,
        country=COUNTRY,
        state=STATE,
        city=CITY,
        zipcode=ZIPCODE,
        mobile=MOBILE,
    )

    # Step 5: Verify account creation
    logger.info("STEP 5: Verify account creation")
    expect(
        page.get_by_text("Account Created!")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Account created successfully")
    logger.info("TEST PASSED: Create a new user account")