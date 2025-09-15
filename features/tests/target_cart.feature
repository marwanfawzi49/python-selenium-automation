Feature: Add Target product to cart

  Scenario Outline: Add a product and verify it is in the cart
    Given open Target homepage
    When search for <product>
    When add the product to the cart
    Then the product appears in the cart (via total price)

    Examples:
      | product |
      | tea     |


