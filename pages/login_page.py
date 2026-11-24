import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    LOGIN_URL = "https://automationexercise.com/login"

    def open_login_page(self):
        logger.info("ACTION: Open login page")
        self.open(self.LOGIN_URL)

    def login(self, email: str, password: str):
        logger.info("ACTION: Enter login email")
        self.fill(
            'form[action="/login"] input[type="email"]',
            email
        )

        # Never log the password value.
        logger.info("ACTION: Enter login password")
        self.fill(
            'form[action="/login"] input[type="password"]',
            password
        )

        logger.info("ACTION: Click Login button")
        self.click('form[action="/login"] button[type="submit"]')

    def signup(self, name: str, email: str):
        logger.info("ACTION: Enter signup name")
        self.fill(
            'form[action="/signup"] input[name="name"]',
            name
        )

        logger.info("ACTION: Enter signup email")
        self.fill(
            'form[action="/signup"] input[type="email"]',
            email
        )

        logger.info("ACTION: Click Signup button")
        self.click('form[action="/signup"] button[type="submit"]')