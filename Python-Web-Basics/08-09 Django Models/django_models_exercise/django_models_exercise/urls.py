"""
 !!!!!!!!!!!!!!!!!!!!!!!!!  MAIN URLS  !!!!!!!!!!!!!!!!!!!!!!!

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin panel'),
    path('', include('django_models_exercise.shipyard.urls'))
]
