import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers

logger = logging.getLogger(__name__)

scenarios("../features/search_no_results.feature")


@given("the user navigates to the products page directly")
def navigate_to_products_directly(page: Page):
    logger.info("ACTION: Navigate directly to products page")
    page.goto("https://automationexercise.com/products")
    expect(page).to_have_url("https://automationexercise.com/products")


@when(parsers.parse('the user searches for nonexistent product "{product_name}"'))
def search_nonexistent_product(page: Page, product_name: str):
    logger.info("ACTION: Search nonexistent product: %s", product_name)
    page.get_by_placeholder("Search Product").fill(product_name)
    page.locator("#submit_search").click()


@then("no products should be displayed in the results")
def verify_no_products_displayed(page: Page):
    logger.info("ASSERTION: Verify 0 products displayed")
    expect(page.locator(".productinfo p")).to_have_count(0)
