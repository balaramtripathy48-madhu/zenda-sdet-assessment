Feature: Product Search
  As a customer
  I want to search for products
  So that I can find the items I wish to purchase

  Scenario: Search for an existing product
    Given the user is on the products page
    When the user searches for product "Blue Top"
    Then "Blue Top" should be visible in the search results
