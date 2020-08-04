from django.test import TestCase
from ghibli_movies.utils import ghibli_client
import json


class APITextCase(TestCase):
    def test_api_server_data_structure(self):
        client = ghibli_client.GhibliClient()

        people = json.loads(client.get_people().text)

        assert all('id' in person for person in people), 'id field does not exits in People in API'
        assert all('name' in person for person in people), 'name field does not exits in People in API'
        assert all('films' in person for person in people), 'films field does not exits in People in API'
