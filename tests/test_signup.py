import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then
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

scenarios("../features/signup.feature")


@when("the user clicks on the Signup / Login link")
def click_signup_login_link(page: Page):
    logger.info("ACTION: Click Signup / Login link")
    page.get_by_role("link", name="Signup / Login").click()


@then('the "New User Signup!" heading should be visible')
def verify_new_user_signup_heading(page: Page):
    logger.info("ASSERTION: Verify New User Signup heading")
    expect(page.get_by_text("New User Signup!")).to_be_visible()


@when("the user enters a valid name and unique email")
def enter_valid_name_and_email(page: Page):
    logger.info("ACTION: Enter name and unique email")
    page.get_by_placeholder("Name").fill(SIGNUP_NAME)
    page.locator('form[action="/signup"] input[type="email"]').fill(generate_unique_email())


@when("the user submits the signup form")
def submit_signup_form(page: Page):
    logger.info("ACTION: Click Signup button")
    page.get_by_role("button", name="Signup").click()


@then('the "Enter Account Information" page should be visible')
def verify_enter_account_info_page(page: Page):
    logger.info("ASSERTION: Verify Enter Account Information page")
    expect(page.get_by_text("Enter Account Information")).to_be_visible()


@given("the user opens the signup page")
def open_signup_page(page: Page):
    logger.info("ACTION: Open signup page")
    signup_page = SignupPage(page)
    signup_page.open_signup_page()


@when("the user enters signup details with a unique email")
def enter_signup_details(page: Page):
    logger.info("ACTION: Enter signup name and unique email")
    signup_page = SignupPage(page)
    signup_page.enter_signup_details(SIGNUP_NAME, generate_unique_email())
    signup_page.verify_account_information_page()


@when("the user fills in account information and submits")
def fill_account_info_and_submit(page: Page):
    logger.info("ACTION: Fill account info and create account")
    signup_page = SignupPage(page)
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


@then('the "Account Created!" confirmation should be visible')
def verify_account_created(page: Page):
    logger.info("ASSERTION: Verify Account Created!")
    expect(page.get_by_text("Account Created!")).to_be_visible()
