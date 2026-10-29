# Zenda SDET Technical Assessment

## Project Overview

This project contains automated UI tests for the Automation Exercise e-commerce website using Python, Pytest, and Playwright.

The framework is designed to validate key e-commerce user journeys, including user registration, login, product search, cart operations, and checkout navigation.

The project follows the Page Object Model (POM) design pattern to improve test maintainability, reusability, and readability.

## Tools and Technologies

- Python 3.11
- Playwright
- Pytest
- Pytest-xdist for parallel test execution
- Pytest-html for HTML test reporting
- python-dotenv for environment configuration
- Faker for test data generation

## Project Structure

```text
zenda_sdet_assessment/
├── pages/                  # Page Object Model classes
├── tests/                  # Automated test cases
├── test_data/              # Test data and test data generators
├── utils/                  # Configuration and logging utilities
├── config/                  # Configuration files
├── screenshots/             # Failure screenshots
├── reports/                 # HTML reports and execution logs
├── videos/                  # Playwright video recordings
├── conftest.py              # Pytest fixtures and hooks
├── pytest.ini                # Pytest configuration
├── requirements.txt           # Python dependencies
├── .env                     # Local environment settings (not committed)
├── .gitignore                # Git ignore rules
└── README.md                  # Project documentation
```

## Framework Design

The automation framework uses the Page Object Model (POM).

### Pages

The `pages/` directory contains page classes that encapsulate page-specific locators and actions.

Examples:

- LoginPage
- SignupPage
- ProductsPage
- CartPage
- CheckoutPage
- BasePage

### Tests

The `tests/` directory contains automated test cases organized by functionality.

### Test Data

The `test_data/` directory contains test data and utilities for generating unique test values.

### Configuration and Utilities

The framework uses configuration and utility modules to manage environment settings, logging, and reusable functionality.

## Setup

### Prerequisites

- Python 3.11 installed
- PyCharm or another Python IDE
- Git (optional)

### 1. Clone or Download the Project

Open the project folder in PyCharm.

### 2. Install Dependencies

Open the PyCharm terminal and run:

```bash
python -m pip install -r requirements.txt
```

### 3. Install Playwright Chromium

```bash
python -m playwright install chromium
```

### 4. Configure Environment Variables

Create a local `.env` file in the project root.

Configure the required test account credentials:

```text
TEST_EMAIL=your_test_account_email
TEST_PASSWORD=your_test_account_password
```

Use a dedicated test account.

Do not commit the `.env` file or expose credentials in source code, logs, screenshots, or assessment submissions.

## Run Tests

### Run the Complete Test Suite

```bash
python -m pytest -v
```

### Run Tests in Parallel

Run tests using two workers:

```bash
python -m pytest -n 2 -v
```

### Run a Specific Test File

Example:

```bash
python -m pytest tests/test_login.py -v
```

### Run a Specific Test

Example:

```bash
python -m pytest tests/test_login.py::test_valid_login -v
```

## Automated Test Coverage

The automation suite includes tests for the following areas:

### User Registration

- New user signup
- Signup with generated test data
- Duplicate or invalid signup scenarios

### Login

- Valid login
- Invalid login
- Login verification

### Product Search

- Search for an existing product
- Search with no matching results

### Cart Operations

- Add product to cart
- Verify cart contents
- Update product quantity
- Remove product from cart

### Checkout

- Checkout navigation
- Checkout details for a logged-in user
- Checkout access without completing a real payment

### End-to-End User Journey

The end-to-end test validates a user journey involving:

1. User registration
2. Login
3. Product search
4. Product selection
5. Add product to cart
6. Cart validation
7. Checkout navigation

## Test Reports and Evidence

### Generate an HTML Report

Run:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

The report is generated at:

```text
reports/report.html
```

Open the report in a browser to review the test execution results.

### Execution Logs

Test execution logs are saved in:

```text
reports/test_execution.log
```

### Failure Screenshots

Screenshots captured during test failures are saved in:

```text
screenshots/
```

### Playwright Video Recordings

Test video recordings are saved in:

```text
videos/
```

## Test Execution

The framework uses Pytest fixtures to manage browser and page setup.

The tests run against Chromium using Playwright.

Logging is used to record test execution steps and relevant actions.

Failure screenshots and video recordings provide additional evidence for debugging.

## Known Limitations

- Tests are intended for practice and assessment purposes.
- The test suite uses the public Automation Exercise website, which may change independently of the project.
- Signup tests use generated test data to avoid duplicate account conflicts.
- Checkout tests validate navigation and checkout details without completing a real purchase.
- The missing-required-information checkout scenario should be considered incomplete until its expected validation behavior is explicitly asserted.
- The framework does not perform real payments.

## Security and Test Data

- Use dedicated test accounts.
- Store credentials in local environment variables.
- Do not commit `.env` files.
- Do not hardcode passwords or sensitive information in test files.
- Do not perform real purchases or payments.

## Assessment Deliverables

The project contains the UI automation framework and automated test cases for the e-commerce scenarios.

The manual risk-based testing and payment incident analysis for the School Management Platform are separate assessment deliverables and should be submitted separately if required by the assessment instructions.

## Author

Zenda SDET Technical Assessment
