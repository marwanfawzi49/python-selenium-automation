# Created by marwan ismael  at 9/8/2025
Feature: Target search

  Scenario Outline: search shows matching result
    Given open Target homepage
    When search for <product>
    Then see result for <product>

    Examples:
      | product |
      | tea     |
      | laptop  |
      | mug     |

