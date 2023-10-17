# app_auth_urls
from django.urls import path

from user_and_pass_manager_lab.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, UserListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('', UserListView.as_view(), name='users_list_user'),
]

# yanko1   .M*YD6jgdnC.sgj
