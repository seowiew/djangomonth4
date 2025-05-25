from django.urls import path
from .views import (
    FilmListView,
    FilmDetailView,
    FilmCreateView,
    FilmUpdateView,
    FilmDeleteView,
    FilmSearchView
)

app_name = 'films'

urlpatterns = [
    path('', FilmListView.as_view(), name='film_list'),
    path('<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('create/', FilmCreateView.as_view(), name='film_create'),
    path('<int:pk>/update/', FilmUpdateView.as_view(), name='film_update'),
    path('<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete'),
    path('search/', FilmSearchView.as_view(), name='film_search' ),
]