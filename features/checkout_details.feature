Feature: Logged-in User Checkout Details
  As a logged-in user
  I want to proceed to checkout
  So that I can see the order address and review details

  Scenario: Logged-in user verifies checkout details
    Given the user is logged in with test credentials
    When the user adds the first product to the cart
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    And the user proceeds to checkout
    Then the "Address Details" section should be visible
    And the "Review Your Order" section should be visible
