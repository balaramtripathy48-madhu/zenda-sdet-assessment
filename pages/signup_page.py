import logging

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.config_reader import get_base_url

logger = logging.getLogger(__name__)


class SignupPage(BasePage):

    def open_signup_page(self):
        logger.info("Opening signup page")

        self.page.goto(get_base_url())

        self.page.get_by_role(
            "link",
            name="Signup / Login"
        ).click()

    def enter_signup_details(self, name, email):
        logger.info("Entering signup name and email")

        self.page.get_by_placeholder("Name").fill(name)

        self.page.locator(
            'form[action="/signup"] input[type="email"]'
        ).fill(email)

        logger.info("Submitting signup form")

        self.page.get_by_role(
            "button",
            name="Signup"
        ).click()

    def verify_account_information_page(self):
        logger.info("Verifying account information page")

        expect(
            self.page.get_by_text("Enter Account Information")
        ).to_be_visible()

    def fill_account_information(
        self,
        password,
        first_name,
        last_name,
        address,
        country,
        state,
        city,
        zipcode,
        mobile
    ):
        logger.info("Filling account information")

        self.page.locator("#password").fill(password)
        self.page.locator("#first_name").fill(first_name)
        self.page.locator("#last_name").fill(last_name)
        self.page.locator("#address1").fill(address)

        self.page.locator("#country").select_option(label=country)

        self.page.locator("#state").fill(state)
        self.page.locator("#city").fill(city)
        self.page.locator("#zipcode").fill(zipcode)
        self.page.locator("#mobile_number").fill(mobile)

        logger.info("Submitting account information")

        self.page.get_by_role(
            "button",
            name="Create Account"
        ).click()