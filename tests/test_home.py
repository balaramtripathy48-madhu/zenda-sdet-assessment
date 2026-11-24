from playwright.sync_api import Page, expect
from utils.logger import get_logger

logger = get_logger(__name__)


def test_homepage_loads(page: Page):
    logger.info("Starting homepage test")

    page.goto(page.base_url)

    expect(page).to_have_title("Automation Exercise")

    logger.info("Homepage loaded successfully")
