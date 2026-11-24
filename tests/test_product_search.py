import logging
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages.products_page import ProductsPage

logger = logging.getLogger(__name__)

scenarios("../features/product_search.feature")


@given("the user is on the products page")
@when("the user navigates to the products page")
def user_on_products_page(page: Page):
    logger.info("ACTION: Open products page")
    products_page = ProductsPage(page)
    products_page.open_products_page()


@when(parsers.parse('the user searches for product "{product_name}"'))
def search_product_by_name(page: Page, product_name: str):
    logger.info("ACTION: Search for product: %s", product_name)
    products_page = ProductsPage(page)
    products_page.search_product(product_name)


@then(parsers.parse('"{product_name}" should be visible in the search results'))
def verify_product_visible_in_results(page: Page, product_name: str):
    logger.info("ASSERTION: Verify %s is in search results", product_name)
    expect(page.get_by_text(product_name, exact=True).first).to_be_visible()
