Feature: Product Search Without Results
  As a customer
  I want to search for a product that does not exist
  So that I can verify no matching products are returned

  Scenario: Search for a nonexistent product
    Given the user navigates to the products page directly
    When the user searches for nonexistent product "XYZNonexistentProduct123"
    Then no products should be displayed in the results
