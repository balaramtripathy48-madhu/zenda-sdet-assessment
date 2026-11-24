Feature: Update Cart Quantity
  As a customer
  I want to update the quantity on the product details page
  So that I can add multiple units of a product to my cart

  Scenario: Update cart quantity from product details
    Given the user navigates to product details for product "1"
    When the user sets the product quantity to "2"
    And the user clicks Add to Cart on product details
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    Then the cart quantity should be "2"
