import requests
import random
import string

class NoteFactory:
    @staticmethod
    def generate_random_title(length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def generate_random_content(length=50):
        return ''.join(random.choices(string.ascii_letters + ' ', k=length))

    @classmethod
    def create_random_note(cls):
        return {
            "title": cls.generate_random_title(),
            "content": cls.generate_random_content()
        }

    @classmethod
    def create_predefined_note(cls, title="Тестовая заметка", content="Контент тестовой заметки"):
        return {
            "title": title,
            "content": content
        }

class NotesPage:
    BASE_URL = "http://127.0.0.1:8000"

    def _url(self, endpoint=""):
        return f"{self.BASE_URL}/notes{endpoint}"

    def create_note(self, note_data):
        return requests.post(self._url("/"), json=note_data)

    def get_all_notes(self):
        return requests.get(self._url("/"))

    def get_note(self, note_id):
        return requests.get(self._url(f"/{note_id}/"))

    def update_note(self, note_id, note_data):
        return requests.put(self._url(f"/{note_id}/"), json=note_data)

    def delete_note(self, note_id):
        return requests.delete(self._url(f"/{note_id}/"))