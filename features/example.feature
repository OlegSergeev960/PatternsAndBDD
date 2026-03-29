1. Создание заметок:
a) Успешное создание заметки с валидными данными
    Feature: note creation
    Scenario: note has been created successfully
    Given: the note payload with title “Test” and content "This is a
           note"
    When: send a request to create a note
    Then: the response status code should be 200
    And: the response should contain the correct title

b) Неуспешное создание заметки с не валидными данными
    Feature: note creation failed
    Scenario: note has not been created
    Given: the user press button "Create new note"
    When: send a request to create a note
    Then: the response status code should be 404
    And: the response should contain the correct title

2. Получение списка заметок:
a) Когда заметок нет
    Feature: get notes list
    Scenario: get empty list
    Given: the user is on the main page
    When: send a request to get notes list
    Then: the response status code should be 422
    And: the response should contain the correct title

b) Когда заметки есть
    Feature: get notes list
    Scenario: get user notes list
    Given: the user is on the main page
    When: send a request to get notes list
    Then: the response status code should be 200
    And: the response should contain the correct title

3. Получение заметки по id:
a) По валидному id
    Feature: get note id
    Scenario: get valid note id
    Given: the user is in the notes list
    When: send a request to get note id
    Then: the response status code should be 200
    And: the response should contain the correct title

b) По не валидному id
    Feature: get note id
    Scenario: get invalid note id
    Given: the user is in the notes list
    When: send a request to get note id
    Then: the response status code should be 422
    And: the response should contain the correct title

4. Редактирование заметки по id
a) По валидному id
    Feature: editing note
    Scenario: edit valid note id
    Given: the user is in the notes list
    When: send a request to edit note
    Then: the response status code should be 200
    And: the response should contain the correct title

b) По не валидному id
    Feature: editing note
    Scenario: edit invalid note id
    Given: the user is in the notes list
    When: send a request to edit note
    Then: the response status code should be 422
    And: the response should contain the correct title

5. Удаление заметки по id
a) По валидному id
    Feature: deleting note
    Scenario: delete valid note id
    Given: the user is in the notes list
    When: send a request to delete note
    Then: the response status code should be 200
    And: the response should contain the correct title

b) По не валидному id
    Feature: deleting note
    Scenario: delete invalid note id
    Given: the user is in the notes list
    When: send a request to delete note
    Then: the response status code should be 422
    And: the response should contain the correct title