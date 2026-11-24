import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class CheckoutPage(BasePage):

    def proceed_to_checkout(self):
        logger.info("ACTION: Click Proceed To Checkout")
        self.click('a:has-text("Proceed To Checkout")')

    def register_or_login(self):
        logger.info("ACTION: Click Register / Login")
        self.click('a:has-text("Register / Login")')

    def place_order(self):
        logger.info("ACTION: Click Place Order")
        self.click('a:has-text("Place Order")')

    def fill_comment(self, comment: str):
        logger.info("ACTION: Enter comment in checkout message field")
        self.fill("textarea[name='message']", comment)