from django.urls import path
from final_exam_recheck.ProfileApp.views import profile_create, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('create/', profile_create, name='profile create'),
    path('details/', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
]
