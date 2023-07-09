from django.urls import path

from django_forms.forms_web.views import index, model_form_view

urlpatterns = [
    path('', index, name='index'),
    path('model-form/', model_form_view, name='model-form'),
]
