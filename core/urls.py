from django.urls import path

from . import views     


app_name = 'core'
urlpatterns = [
    path('movies',
        views.MoviesList.as_view(),
        name='MoviesList'),
    path('movies/<int:pk>',
        views.MoviesDetail.as_view(),
        name='MoviesDetail'),
    path('movies/<int:movie_id>/vote/',
        views.CreateVote.as_view(),
        name='CreateVote'),
    path('movies/<int:movie_id>/vote/<int:pk>/',
        views.UpdateVote.as_view(),
        name='UpdateVote'),
]