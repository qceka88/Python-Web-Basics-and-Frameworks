"""
Auth Flow:
--Authentication--

The user sent credentials to a  system
 - username & password, phone number + sms code, authentication app


    -- We can add custom authentications written by us

-- Authorization
    - after authentications, system authorizate user





"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('autetications_authorisation_lab.web.urls')),
]
