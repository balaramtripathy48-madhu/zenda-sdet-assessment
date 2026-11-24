Feature: User Signup
  As a new user
  I want to register an account
  So that I can use the platform services

  Scenario: Verify signup page loads
    Given the user is on the homepage
    When the user clicks on the Signup / Login link
    Then the "New User Signup!" heading should be visible

  Scenario: Verify signup form submission
    Given the user is on the homepage
    When the user clicks on the Signup / Login link
    And the user enters a valid name and unique email
    And the user submits the signup form
    Then the "Enter Account Information" page should be visible

  Scenario: Create a new user account
    Given the user opens the signup page
    When the user enters signup details with a unique email
    And the user fills in account information and submits
    Then the "Account Created!" confirmation should be visible
