Feature: Home Page
  As a user
  I want to access the Automation Exercise website
  So that I can verify the homepage loads correctly

  Scenario: Homepage loads successfully
    Given the user navigates to the homepage
    Then the page title should be "Automation Exercise"
