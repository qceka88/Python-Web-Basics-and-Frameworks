from django.urls import path


from django_rest_lab.web.views import WebView


urlpatterns = [
    path('', WebView.as_view(), name='index view'),
]
