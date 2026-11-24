import logging

from playwright.sync_api import Page, expect

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


def test_end_to_end_user_journey(page: Page):
    logger.info("========== E2E TEST START ==========")

    # STEP 1: Create a new account
    logger.info("STEP 1: Initialize SignupPage")
    signup_page = SignupPage(page)

    logger.info("STEP 2: Open signup page")
    signup_page.open_signup_page()

    logger.info("STEP 3: Enter signup name and unique email")
    signup_page.enter_signup_details(
        SIGNUP_NAME,
        generate_unique_email(),
    )

    logger.info("STEP 4: Verify account information page")
    signup_page.verify_account_information_page()

    logger.info("STEP 5: Fill account information and create account")
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

    logger.info("STEP 6: Verify account creation")
    expect(
        page.get_by_text("Account Created!")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Account created successfully")

    # STEP 2: Continue after account creation
    logger.info("STEP 7: Click Continue after account creation")
    page.get_by_role("link", name="Continue").click()

    logger.info("STEP 8: Verify user is logged in")
    expect(
        page.get_by_text("Logged in as", exact=False)
    ).to_be_visible()

    logger.info("ASSERTION PASSED: User logged in successfully")

    # STEP 3: Search for product
    logger.info("STEP 9: Initialize ProductsPage")
    products_page = ProductsPage(page)

    logger.info("STEP 10: Open products page")
    products_page.open_products_page()

    logger.info("STEP 11: Search for product Blue Top")
    products_page.search_product("Blue Top")

    logger.info("STEP 12: Verify Blue Top appears in search results")
    expect(
        page.get_by_text("Blue Top", exact=True).first
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Blue Top is visible in search results")

    # STEP 4: Select product
    logger.info("STEP 13: Select the first product")
    products_page.select_first_product()

    logger.info("STEP 14: Verify product details page opened")
    expect(
        page.locator("#quantity")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Product details page is visible")

    # STEP 5: Add product to cart
    logger.info("STEP 15: Click Add to Cart")
    page.get_by_role("button", name="Add to cart").click()

    logger.info("STEP 16: Verify product-added confirmation")
    expect(
        page.get_by_text("Your product has been added to cart")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Product added to cart")

    # STEP 6: Open cart
    logger.info("STEP 17: Initialize CartPage")
    cart_page = CartPage(page)

    logger.info("STEP 18: Open cart from confirmation popup")
    cart_page.view_cart_from_popup()

    logger.info("STEP 19: Verify product is in cart")
    expect(
        cart_page.get_cart_products()
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Product is visible in cart")

    # STEP 7: Proceed to checkout
    logger.info("STEP 20: Proceed to checkout")
    cart_page.proceed_to_checkout()

    logger.info("STEP 21: Verify Address Details section")
    expect(
        page.get_by_text("Address Details")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Address Details is visible")

    logger.info("STEP 22: Verify Review Your Order section")
    expect(
        page.get_by_text("Review Your Order")
    ).to_be_visible()

    logger.info("ASSERTION PASSED: Review Your Order is visible")

    # Do not place an order or make a payment
    logger.info("STEP 23: Stop before placing an order or payment")

    logger.info("========== E2E TEST PASSED ==========")