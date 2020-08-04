from ghibli_movies.utils import ghibli_client
from django.core.cache import cache
from workers import task
from logging import getLogger
import json

logger = getLogger(__name__)


@task(schedule=50)  # In seconds
def sync_movies():
    client = ghibli_client.GhibliClient()

    # Retrieving directly people endpoint , since people information in Ghibli API in movies endpoint is
    # not reliable
    people = json.loads(client.get_people().text)

    for person in people:
        # Get films of the person
        films = person.get('films')

        person_id = person.get('id')

        for film in films:
            # Movies are in URL format instead of film id
            film_detail = json.loads(client.get_endpoint(film).text)
            film_id = film_detail.get('id')

            movie = {
                'id': film_detail.get('id'),
                'title': film_detail.get('title'),
                'release_date': film_detail.get('release_date'),
                'rt_score': film_detail.get('rt_score'),
                'people': []
            }

            if cache.get(f'movie_{film_id}') is None:
                # Insert if film is not stored yet
                movie['people'].append({
                    'id': person_id,
                    'name': person.get('name'),
                })
                cache.set(f'movie_{film_id}', movie)
            else:
                # If movie already stored, get movie detail in order to add person
                current_movie = cache.get(f'movie_{film_id}')

                # Add person to film if it is not exited
                if not any(person_id in person['id'] for person in current_movie['people']):
                    current_movie['people'].append({
                        'id': person_id,
                        'name': person.get('name'),
                    })

                    cache.set(f'movie_{film_id}', current_movie)

    logger.debug('Movies synchronized.')


