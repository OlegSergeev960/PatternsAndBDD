Feature: Deleting an existing note

    Scenario: Successful note deletion
    Given that there is a note with ID 1 in the system
    When a request to delete a note with ID 1 is sent
    Then the response should have a 200 OK status
    And the response body should contain "Note deleted"

    Scenario: Attempting to delete a non-existent note
    Given that there is no note with ID 999 in the system
    When a request to delete a note with ID 999 is sent
    Then the response should have a 404 Not Found status