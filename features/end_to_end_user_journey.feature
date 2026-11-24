Feature: End-to-End User Journey
  As a new customer
  I want to register an account, search for a product, add it to cart, and reach checkout
  So that the entire purchasing flow is verified

  Scenario: Complete end-to-end user journey
    Given a new user registers an account successfully
    When the user clicks Continue after account creation
    Then the user should see "Logged in as"
    When the user navigates to the products page
    And the user searches for product "Blue Top"
    Then "Blue Top" should be visible in the search results
    When the user selects the first product
    And the user clicks Add to Cart on product details
    Then the product-added confirmation popup should be visible
    When the user opens the cart from the popup
    Then the product should be displayed in the cart
    When the user proceeds to checkout
    Then the "Address Details" section should be visible
    And the "Review Your Order" section should be visible
