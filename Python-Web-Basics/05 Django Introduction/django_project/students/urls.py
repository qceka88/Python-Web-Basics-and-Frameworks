from django.urls import path
from django_project.students import views

urlpatterns = [
    path('', views.home_view)
]
