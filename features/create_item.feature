
Feature: Create inventory item
  As a QA engineer
  I want to add items via the API
  So that I can track stock levels

  Scenario Outline: Successful item creation
    Given the server is running at "http://localhost:5001"
    When I create an item with name "<name>" and qty <qty>
    Then the status code is 201
    And the response contains an id

    Examples:
      | name   | qty |
      | Widget | 5   |
      | Gadget | 2   |