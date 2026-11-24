import pytest
import os
from playwright.sync_api import Playwright

from utils.config_reader import get_base_url, get_browser, get_headless
from utils.logger import get_logger


logger = get_logger(__name__)


@pytest.fixture
def browser_context(playwright: Playwright):
    browser_name = get_browser()

    logger.info(f"Launching browser: {browser_name}")

    browser_type = getattr(playwright, browser_name)
    browser = browser_type.launch(headless=get_headless())

    context = browser.new_context(
    record_video_dir="videos/")
    yield context

    context.close()
    browser.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()

    # Store the configured website URL for tests
    page.base_url = get_base_url()

    yield page

    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Log the test result
    if report.when == "call":
        logger.info(
            "TEST RESULT: %s - %s",
            item.nodeid,
            report.outcome.upper()
        )

    # Capture screenshot if the test fails
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            logger.error(
                "Test failed. Screenshot saved: %s",
                screenshot_path
            )