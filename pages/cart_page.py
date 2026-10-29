import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class CartPage(BasePage):
    CART_URL = "https://automationexercise.com/view_cart"

    def add_first_product_to_cart(self):
        logger.info("ACTION: Locate the first product on the page")
        product = self.page.locator(".product-image-wrapper").first

        logger.info("ACTION: Hover over the first product")
        product.hover()

        logger.info("ACTION: Click Add to Cart for the first product")
        product.locator(".add-to-cart").first.click()

    def open_cart(self):
        logger.info("ACTION: Open the shopping cart")
        self.open(self.CART_URL)

    def view_cart_from_popup(self):
        logger.info("ACTION: Click View Cart in the confirmation popup")
        self.page.get_by_text("View Cart", exact=True).click()

    def proceed_to_checkout(self):
        logger.info("ACTION: Click Proceed To Checkout")
        self.click('a:has-text("Proceed To Checkout")')

    def remove_product(self):
        logger.info("ACTION: Remove product from cart")
        self.click(".cart_quantity_delete")

    def get_cart_products(self):
        logger.info("ACTION: Locate products in the cart")
        return self.page.locator(".cart_description")

    def get_cart_quantity(self):
        logger.info("ACTION: Locate cart quantity")
        return self.page.locator(".cart_quantity")