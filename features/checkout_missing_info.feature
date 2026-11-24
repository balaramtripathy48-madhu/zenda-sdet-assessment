Feature: Checkout Verification
  As a customer
  I want to review the checkout page before placing an order
  So that I verify order details without completing payment

  Scenario: Verify checkout page sections and place order link
    Given the user is logged in with test credentials
    When the user adds the first product to the cart
    And the user opens the cart from the popup
    And the user proceeds to checkout
    Then the "Address Details" section should be visible
    And the "Review Your Order" section should be visible
    And the "Place Order" link should be visible
