import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ProductsPage(BasePage):
    PRODUCTS_URL = "https://automationexercise.com/products"

    def open_products_page(self):
        logger.info("ACTION: Open products page")
        self.open(self.PRODUCTS_URL)

    def search_product(self, product_name: str):
        logger.info("ACTION: Enter product search term")
        self.fill("#search_product", product_name)

        logger.info("ACTION: Click Search button")
        self.click("#submit_search")

    def select_first_product(self):
        logger.info("ACTION: Select the first product")
        self.click(".product-image-wrapper .choose")