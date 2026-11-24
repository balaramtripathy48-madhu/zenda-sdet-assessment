Feature: Cart Quantity
  As a customer
  I want to verify the product quantity in the cart
  So that I can be sure the correct quantity was added

  Scenario: Verify cart quantity is accurate
    Given the user is on the homepage
    When the user adds the first product to the cart
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    Then the product should be displayed in the cart
    And the cart quantity should be "1"
