Feature: Update and delete inventory items
  Scenario: Update an existing item
    Given the server is running at "http://localhost:5000"
    And an item exists with name "Orig" and qty 3
    When I update item <id> to name "Updated" and qty 8
    Then the status code is 200
    And the response JSON name is "Updated"

  Scenario: Delete an existing item
    Given the server is running at "http://localhost:5000"
    And an item exists with name "DelMe" and qty 1
    When I delete item <id>
    Then the status code is 204