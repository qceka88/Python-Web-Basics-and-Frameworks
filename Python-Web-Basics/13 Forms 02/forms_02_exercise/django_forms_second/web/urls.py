from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django_forms_second.web.views import index, create_image_view

urlpatterns = [
    path('', index, name='index'),
    path('create_image/', create_image_view, name='create-image')
]
