"""
  ###########     Main URL`s     ###########
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_music_app_pre_exam.mymusicapp.urls'))
]
