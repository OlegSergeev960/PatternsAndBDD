Feature: Editing an existing note

    Scenario: Successful note editing
    Given that the system has a note with ID 1 and the title "Old Title"
    When a request is sent to update the note title from ID 1 to "New Title"
    Then the response should have a 200 OK status
    And the title in the response should be "New Title"

    Scenario: Attempt to edit a non-existent note
    Given that the system does not have a note with ID 999
    When a request is sent to update a note with ID 999
    Then the response should have a 404 Not Found status