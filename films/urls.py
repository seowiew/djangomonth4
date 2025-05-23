from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('<int:id>/', views.film_detail, name='film_detail'),
    path('create/', views.film_create, name='film_create'),
    path('<int:id>/edit/', views.film_update, name='film_update'),
    path('<int:id>/delete/', views.film_delete, name='film_delete'),
]
