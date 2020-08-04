from django.conf import settings
from apiclient import APIClient


class GhibliClient(APIClient):
    def get_people(self):
        return self.get(settings.ENDPOINT_PEOPLE)

    def get_movies(self):
        return self.get(settings.ENDPOINT_FILMS)

    def get_endpoint(self, endpoint_url):
        return self.get(endpoint_url)
