from django.urls import path
#from django.views import generic as views

from autetications_authorisation_lab.web.views import index, login_user,logout_user

urlpatterns = [
    #path('', views.TemplateView.as_view(template_name='index.html')),
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
