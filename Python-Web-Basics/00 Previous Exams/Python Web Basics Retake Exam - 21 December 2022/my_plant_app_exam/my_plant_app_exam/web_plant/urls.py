from django.urls import path, include

from my_plant_app_exam.web_plant.views import index, profile_create_page, catalogue, plant_create_page, \
    plant_details_page, plant_edit_page, plant_delete_page, profile_details_page, profile_edit_page, profile_delete_page

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue page'),
    path('create/', plant_create_page, name='plant create page'),
    path('details/<int:pk>/', plant_details_page, name='plant details page'),
    path('edit/<int:pk>/', plant_edit_page, name='plant edit page'),
    path('delete/<int:pk>', plant_delete_page, name='plant delete page'),
    path('profile/', include([
        path('create/', profile_create_page, name='profile create'),
        path('details/', profile_details_page, name='profile details'),
        path('edit/', profile_edit_page, name='profile edit'),
        path('delete/', profile_delete_page, name='profile delete'),
    ])),
]
