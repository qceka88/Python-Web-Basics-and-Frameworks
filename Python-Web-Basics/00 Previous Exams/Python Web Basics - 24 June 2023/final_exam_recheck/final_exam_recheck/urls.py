"""
MAIN URLS
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('final_exam_recheck.MainApp.urls')),
    path('', include('final_exam_recheck.FruitApp.urls')),
    path('profile/', include('final_exam_recheck.ProfileApp.urls')),
]
