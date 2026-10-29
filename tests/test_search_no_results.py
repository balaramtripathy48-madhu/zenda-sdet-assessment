import logging

from playwright.sync_api import Page, expect

logger = logging.getLogger(__name__)


def test_search_nonexistent_product(page: Page):
    logger.info("TEST START: Search for a nonexistent product")

    # Step 1: Open Products page directly to avoid the homepage ad
    logger.info("STEP 1: Navigate directly to the Products page")
    page.goto("https://automationexercise.com/products")

    # Step 2: Verify Products page opened
    logger.info("STEP 2: Verify the Products page URL")
    expect(page).to_have_url(
        "https://automationexercise.com/products"
    )
    logger.info("ASSERTION PASSED: Products page URL is correct")

    # Step 3: Search for a product that does not exist
    logger.info("STEP 3: Enter a nonexistent product name in the search field")
    page.get_by_placeholder("Search Product").fill(
        "XYZNonexistentProduct123"
    )

    logger.info("STEP 4: Click the Search button")
    page.locator("#submit_search").click()

    # Step 4: Verify no products are displayed
    logger.info("STEP 5: Verify no products are displayed in the results")
    expect(page.locator(".productinfo p")).to_have_count(0)
    logger.info("ASSERTION PASSED: No products are displayed")

    logger.info("TEST PASSED: Search for a nonexistent product")