"""

############ MAIN URLS ############

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_collection_app_exam.car_collection.urls'))
]
