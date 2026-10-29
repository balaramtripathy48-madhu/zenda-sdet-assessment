import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        logger.info("ACTION: Open URL: %s", url)
        self.page.goto(url)

    def click(self, selector: str):
        logger.info("ACTION: Click element: %s", selector)
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        # Do not log the value because it could contain sensitive information.
        logger.info("ACTION: Fill field: %s", selector)
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str):
        logger.info("ACTION: Read text from element: %s", selector)
        return self.page.locator(selector).inner_text()