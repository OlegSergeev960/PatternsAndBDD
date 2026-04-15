Feature: Retrieving a note by ID

    Scenario: Retrieving an existing note
    Given that there is a note with ID 1 in the system
    When a request to retrieve a note with ID 1 is sent
    Then the response must have a status of 200 OK
    And the ID in the response must be equal to 1

    Scenario: Attempting to retrieve a non-existent note
    Given that there is no note with ID 999 in the system
    When a request to retrieve a note with ID 999 is sent
    Then the response must have a status of 404 Not Found


