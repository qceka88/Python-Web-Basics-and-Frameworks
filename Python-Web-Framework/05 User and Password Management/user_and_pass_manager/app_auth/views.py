from django import forms
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _

# Create your views here.
# app_auth

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Please repeat Passowrd!"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'IT WORKS'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # static way of providing 'success_url'
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result

    # dymanic way of providing 'success_url'
    # def get_success_url(self):
    #     pass
    #
    # def get_form_class(self):
    #     ...


class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    # extra_context = {'title': 'login', 'link_title': 'register'}


class LogoutUserView(auth_views.LogoutView):
    ...




@login_required
def func_view(request):
    ...


class ViewWithPermission(auth_mixins.PermissionDenied, views.TemplateView):
    template_name = 'app_auth/users_list.html'


class UserListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'
    # login_url = '....'
