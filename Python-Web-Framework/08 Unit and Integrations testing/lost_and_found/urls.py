"""Lost_and_Found URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lost_and_found.objects_posts.urls')),
    path('accounts/', include('lost_and_found.accounts.urls')),
]
