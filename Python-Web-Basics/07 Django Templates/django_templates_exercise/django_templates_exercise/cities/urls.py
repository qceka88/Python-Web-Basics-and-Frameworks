from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_templates_exercise.cities import views
from django_templates_exercise.cities.views import city_by_data, no_such_city, exercise

urlpatterns = [
    path('', views.all_cities, name='all cities'),
    path('<city_data>/', city_by_data, name='city by name'),
    path('error', no_such_city, name='no such city'),
    path('exercise/test/', exercise, name='exercise')
]
