from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('django_rest_lab.api.urls')),
    path('', include('django_rest_lab.web.urls')),
]
