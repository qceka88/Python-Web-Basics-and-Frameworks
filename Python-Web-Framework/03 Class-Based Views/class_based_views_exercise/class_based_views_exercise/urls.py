from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('class_based_views_exercise.WebCBV.urls')),
]
