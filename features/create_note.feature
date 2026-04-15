Feature: Creating a new note

Scenario: Successful note creation
Given that the user enters data for the new note
When the note creation request is sent
Then the response should have a 201 Created status
And the response should contain the ID of the created note

Scenario: Creating a note with a missing title
Given that the user does not enter a title for the note
When the note creation request is sent
Then the response should have a 400 Bad Request status