# Created by marwan ismael 1987 at 9/19/2025
Feature: Tests for Cart functionality

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

