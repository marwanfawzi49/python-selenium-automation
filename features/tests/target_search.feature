# Created by marwan ismael  at 9/19/2025
Feature: Tests for Target search functionality


  Scenario: User can search for a product in target
    Given Open target main page
    When Search for a product
    Then Verify search results are shown