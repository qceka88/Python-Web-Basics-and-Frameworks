from django.urls import path

from async_operations.thumbnailer.views import index, index_slow, transcribe

urlpatterns = (
    path('', index, name='index'),
    path('slow/', index_slow, name='index_slow'),
    path('transcribe/<int:pk>/', transcribe, name='transcribe'),
)