from django.urls import path, include

from car_collection_app_exam.car_collection.views import index, profile_create, catalogue_page, car_create, car_details, \
    car_edit, car_delete, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', index, name='index page'),
    path('profile/', include([
        path('create/', profile_create, name='profile create page'),
        path('details/', profile_details, name='profile details page'),
        path('edit/', profile_edit, name='profile edit page'),
        path('delete/', profile_delete, name='profile delete page'),
    ])),
    path('catalogue/', catalogue_page, name='catalogue page'),
    path('car/', include([
        path('create/', car_create, name='car create page'),
        path('<int:pk>/', include([
            path('details/', car_details, name='car details page'),
            path('edit/', car_edit, name='car edit page'),
            path('delete/', car_delete, name='car delete page'),
        ])),
    ])),
]
