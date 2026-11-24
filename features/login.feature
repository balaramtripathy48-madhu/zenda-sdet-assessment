Feature: User Login
  As a user
  I want to attempt logging into the website
  So that I can verify invalid login attempts are rejected

  Scenario: User attempts login with invalid credentials
    Given the user is on the login page
    When the user submits invalid login credentials
    Then an error message "Your email or password is incorrect!" should be visible
