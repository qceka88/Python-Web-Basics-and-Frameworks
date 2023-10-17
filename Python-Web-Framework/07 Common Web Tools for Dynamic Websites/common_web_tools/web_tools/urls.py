from django.urls import path
from .views import index, create_task, details_task


urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create task'),
    path('details_task/<int:pk>/', details_task, name='details task'),
]

#from .signals import *