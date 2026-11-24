Feature: Remove From Cart
  As a customer
  I want to remove a product from the shopping cart
  So that my cart remains empty

  Scenario: Remove product from cart successfully
    Given the user is on the homepage
    When the user adds the first product to the cart
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    Then the product should be displayed in the cart
    When the user removes the product from the cart
    Then the message "Cart is empty!" should be visible
