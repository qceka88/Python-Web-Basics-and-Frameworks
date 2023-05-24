from django.urls import path
from django_url_views_recheck.bikers.views import empty, bikers, bikers_id, non_existing_biker

urlpatterns = [
    path('', empty),
    path('bikers/', bikers, name='all bikers'),
    path('bikers/<int:some_id>/', bikers_id, name='by id'),
    path('invalid_biker/', non_existing_biker, name='non existing biker')
]
