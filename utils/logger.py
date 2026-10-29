import logging
import os


# Create logs folder if it does not exist
os.makedirs("reports", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="reports/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def get_logger(name):
    return logging.getLogger(name)