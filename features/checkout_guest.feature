Feature: Guest Checkout
  As a guest user
  I want to attempt checkout without logging in
  So that I am prompted to register or log in

  Scenario: Checkout without login prompts for registration or login
    Given the user is on the homepage
    When the user adds the first product to the cart
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    And the user proceeds to checkout
    Then the user is prompted with "Register / Login"
