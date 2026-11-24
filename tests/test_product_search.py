import logging

from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage

logger = logging.getLogger(__name__)


def test_search_product(page: Page):
    logger.info("TEST START: Search for a product")

    # Step 1: Initialize ProductsPage
    logger.info("STEP 1: Initialize ProductsPage")
    products_page = ProductsPage(page)

    # Step 2: Open products page
    logger.info("STEP 2: Open the products page")
    products_page.open_products_page()

    # Step 3: Search for a product
    logger.info("STEP 3: Search for product 'Blue Top'")
    products_page.search_product("Blue Top")

    # Step 4: Verify the search result
    logger.info("STEP 4: Verify that 'Blue Top' appears in the search results")
    expect(
        page.get_by_text("Blue Top", exact=True).first
    ).to_be_visible()
    logger.info("ASSERTION PASSED: 'Blue Top' is visible in search results")

    logger.info("TEST PASSED: Search for a product")