import requests
from behave import given, when, then

BASE_URL = "http://127.0.0.1:8000"


context = {}

def get_note_by_id(note_id):
    return requests.get(f"{BASE_URL}/notes/{note_id}")


def delete_all_notes():
    try:
        notes = requests.get(f"{BASE_URL}/notes").json()
        for note in notes:
            requests.delete(f"{BASE_URL}/notes/{note['id']}")
        return True
    except Exception:
        return False


@given('пользователь вводит данные для новой заметки')
def step_given_user_enters_note_data(context):
    context['request_data'] = {
        "title": "Новая заметка",
        "content": "Контент для теста"
    }

@given('пользователь не вводит заголовок для заметки')
def step_given_user_misses_title(context):
    context['request_data'] = {
        "content": "Контент без заголовка"

    }

@when('отправляется запрос на создание заметки')
def step_when_create_note_request(context):
    response = requests.post(f"{BASE_URL}/notes", json=context['request_data'])
    context['response'] = response

@given('в системе есть хотя бы одна заметка')
def step_given_there_is_at_least_one_note():
    create_resp = requests.post(f"{BASE_URL}/notes", json={"title": "Тест", "content": "123"})

@given('в системе нет ни одной заметки')
def step_given_there_are_no_notes():
    delete_all_notes()

@when('отправляется запрос на получение списка заметок')
def step_when_get_notes_list_request(context):
    context['response'] = requests.get(f"{BASE_URL}/notes")

@given('в системе есть заметка с ID {note_id}')
def step_given_note_exists(note_id):

    @when('отправляется запрос на получение заметки с ID {note_id}')
    def step_when_get_note_request(context, note_id):
        context['response'] = get_note_by_id(note_id)

@when('отправляется запрос на обновление заголовка заметки с ID {note_id} на "{new_title}"')
def step_when_update_note_request(context, note_id, new_title):
    context['response'] = requests.put(
        f"{BASE_URL}/notes/{note_id}",
        json={"title": new_title}
    )

@when('отправляется запрос на удаление заметки с ID {note_id}')
def step_when_delete_note_request(context, note_id):
    context['response'] = requests.delete(f"{BASE_URL}/notes/{note_id}")

@then('ответ должен иметь статус {status_code}')
def step_then_check_status_code(context, status_code):
    assert context['response'].status_code == int(status_code)

@then('в ответе должен быть ID созданной заметки')
def step_then_check_created_note_id(context):
    data = context['response'].json()
    assert 'id' in data and data['id'] > 0

@then('список заметок не должен быть пустым')
def step_then_notes_list_not_empty(context):
    data = context['response'].json()
    assert isinstance(data, list) and len(data) > 0

@then('список заметок должен быть пустым')
def step_then_notes_list_empty(context):
    data = context['response'].json()
    assert isinstance(data, list) and len(data) == 0

@then('ID в ответе должен быть равен {expected_id}')
def step_then_check_note_id(context, expected_id):
    data = context['response'].json()
    assert data.get('id') == int(expected_id)

@then('заголовок в ответе должен быть "{expected_title}"')
def step_then_check_title(context, expected_title):
    data = context['response'].json()
    assert data.get('title') == expected_title

@then('тело ответа должно содержать "{expected_text}"')
def step_then_check_response_text(context, expected_text):
    data = context['response'].json()
    assert expected_text in data.get('detail', '')