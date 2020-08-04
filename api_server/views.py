from django.http import JsonResponse
from django.core.cache import cache


def movies(request):
    films = dict(cache.get_many(cache.keys("movie_*")))

    # Convert dictionary into list for easier usage in Vue
    films_list = {
        'movies': [films[movie_id] for movie_id in films]
    }

    return JsonResponse(films_list)
