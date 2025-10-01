# Created by marwan ismael
Feature: Test to verify Header UI element


  Scenario: Verify header has correct amount og links
    Given Open target main page
    Then Verify header has 6 links

  Scenario: Verify can click on 1st
    Given Open target main page
    When Click on 1st header link
    Then Verify Target circle opens
