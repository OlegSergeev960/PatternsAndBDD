Feature: Getting a list of all notes

    Scenario: Getting a non-empty list of notes
    Given that there is at least one note in the system
    When a request to get a list of notes is sent
    Then the response must have a 200 OK status
    And the list of notes must not be empty

    Scenario: Getting an empty list of notes
    Given that there are no notes in the system
    When a request to get a list of notes is sent
    Then the response must have a 200 OK status
    And the list of notes must be empty