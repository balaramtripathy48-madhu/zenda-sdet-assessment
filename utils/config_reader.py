import os
from dotenv import load_dotenv

# Load settings from the .env file
load_dotenv()


def get_base_url():
    return os.getenv(
        "BASE_URL",
        "https://automationexercise.com/"
    )


def get_browser():
    return os.getenv("BROWSER", "chromium")


def get_headless():
    return os.getenv("HEADLESS", "false").lower() == "true"