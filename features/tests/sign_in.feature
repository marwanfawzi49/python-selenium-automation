Feature: Sign In access for logged-out user

  Scenario: Logged-out user can access Sign In
    Given Open Target homepage
    When Click Account from header
    And From right-side menu, click Sign In
    Then Verify Sign In form is opened

