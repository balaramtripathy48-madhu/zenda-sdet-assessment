Feature: Checkout Navigation
  As a customer
  I want to navigate back to the cart from the checkout page
  So that I can verify my cart items are still intact

  Scenario: Checkout navigation back to cart preserves items
    Given the user is logged in with test credentials
    When the user adds the first product to the cart
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    And the user proceeds to checkout
    Then the "Address Details" section should be visible
    When the user navigates back to the previous page
    Then the cart page should be displayed with URL "https://automationexercise.com/view_cart"
    And the product should be displayed in the cart
