from django.urls import path
from ui import views


urlpatterns = [
    path('movies', views.movies, name='movies'),
]
