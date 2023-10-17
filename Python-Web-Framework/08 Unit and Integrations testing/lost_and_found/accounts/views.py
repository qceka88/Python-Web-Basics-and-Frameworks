from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# Create your views here.
class LoginUserView(auth_views.LoginView):
    template_name = 'loging.html'
    success_url = reverse_lazy('index')


