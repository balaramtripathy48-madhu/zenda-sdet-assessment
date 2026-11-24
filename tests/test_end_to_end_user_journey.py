import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers

from pages.signup_page import SignupPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

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

scenarios("../features/end_to_end_user_journey.feature")


@given("a new user registers an account successfully")
def register_new_user(page: Page):
    logger.info("ACTION: Register new user account")
    signup_page = SignupPage(page)
    signup_page.open_signup_page()
    signup_page.enter_signup_details(SIGNUP_NAME, generate_unique_email())
    signup_page.verify_account_information_page()
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
    expect(page.get_by_text("Account Created!")).to_be_visible()
    logger.info("ASSERTION: Account created successfully")


@when("the user clicks Continue after account creation")
def click_continue(page: Page):
    logger.info("ACTION: Click Continue after account creation")
    page.get_by_role("link", name="Continue").click()


@then('the user should see "Logged in as"')
def verify_logged_in(page: Page):
    logger.info("ASSERTION: Verify Logged in as is visible")
    expect(page.get_by_text("Logged in as", exact=False)).to_be_visible()


@when("the user navigates to the products page")
def nav_to_products(page: Page):
    logger.info("ACTION: Navigate to products page")
    products_page = ProductsPage(page)
    products_page.open_products_page()


@when(parsers.parse('the user searches for product "{product_name}"'))
def search_product(page: Page, product_name: str):
    logger.info("ACTION: Search for product: %s", product_name)
    products_page = ProductsPage(page)
    products_page.search_product(product_name)


@then(parsers.parse('"{product_name}" should be visible in the search results'))
def verify_product_search_result(page: Page, product_name: str):
    logger.info("ASSERTION: Verify %s in search results", product_name)
    expect(page.get_by_text(product_name, exact=True).first).to_be_visible()


@when("the user selects the first product")
def select_first_product(page: Page):
    logger.info("ACTION: Select first product")
    products_page = ProductsPage(page)
    products_page.select_first_product()
    expect(page.locator("#quantity")).to_be_visible()


@when("the user clicks Add to Cart on product details")
def click_add_to_cart(page: Page):
    logger.info("ACTION: Click Add to Cart button")
    page.get_by_role("button", name="Add to cart").click()
