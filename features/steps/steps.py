import json

import requests
from behave import given, when, then

BASE_URL = "http://127.0.0.1:8000"

@given('the note payload with title “{title}” and content "{content}"')
def step_given_note_payload(context, title, content):
    context.note_payload = {
        "title": title,
        "content": content
    }

@given('the user press button "Create new note"')
def step_given_press_button(context):
    context.note_payload = {"title": "", "content": ""}

@given('the user is on the main page')
def step_given_main_page(context):
    pass

@given('the user is in the notes list')
def step_given_notes_list(context):
    pass

@when('send a request to create a note')
def step_when_create_note(context):
    url = f"{BASE_URL}/notes"
    context.response = requests.post(url, json=context.note_payload)

@when('send a request to get notes list')
def step_when_get_notes_list(context):
    url = f"{BASE_URL}/notes"
    context.response = requests.get(url)

@when('send a request to get note id')
def step_when_get_note_id(context):
    if not hasattr(context, 'note_id') or not context.note_id:
        context.note_id = 1
    url = f"{BASE_URL}/notes/{context.note_id}"
    context.response = requests.get(url)

@when('send a request to edit note')
def step_when_edit_note(context):
    if not hasattr(context, 'note_id') or not context.note_id:
        context.note_id = 1
    url = f"{BASE_URL}/notes/{context.note_id}"
    context.response = requests.put(url, json=context.note_payload)

@when('send a request to delete note')
def step_when_delete_note(context):
    if not hasattr(context, 'note_id') or not context.note_id:
        context.note_id = 1
        if 'invalid' in context.tags:
            context.note_id = 999999
    url = f"{BASE_URL}/notes/{context.note_id}"
    context.response = requests.delete(url)

@then('the response status code should be {status_code}')
def step_then_check_status_code(context, status_code):
    expected_code = int(status_code)
    assert context.response.status_code == expected_code, \
        f"Expected status code {expected_code}, but got {context.response.status_code}"

@then('the response should contain the correct title')
def step_then_check_title_in_response(context):
    response_json = context.response.json()

    if context.note_payload and 'title' in context.note_payload:
        assert 'title' in response_json, "Response does not contain 'title' field"
        assert response_json['title'] == context.note_payload['title'], \
            f"Expected title '{context.note_payload['title']}', but got '{response_json['title']}'"

