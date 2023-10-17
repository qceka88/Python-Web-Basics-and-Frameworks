"""
MAIN URLS
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_and_pass_manager_lab.web.urls')),
    path('auth/', include('user_and_pass_manager_lab.app_auth.urls')),
]
