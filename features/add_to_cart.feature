Feature: Add to Cart
  As a customer
  I want to add a product to my shopping cart
  So that I can purchase it later

  Scenario: Add product to cart successfully
    Given the user is on the homepage
    When the user adds the first product to the cart
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    Then the product should be displayed in the cart
