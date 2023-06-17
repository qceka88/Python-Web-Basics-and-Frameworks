from django.urls import path
from .views import index, add_note_page, edit_note_page, delete_note_page, note_details_page, profile_page, profile_delete

urlpatterns = [
    path('', index, name='home page'),
    path('add/', add_note_page, name='add note page'),
    path('edit/<int:pk>/', edit_note_page, name='edit note page'),
    path('delete/<int:pk>/', delete_note_page, name='delete note page'),
    path('details/<int:pk>/', note_details_page, name='details note page'),
    path('profile/', profile_page, name='profile page'),
    path('profile/delete/', profile_delete, name='profile delete'),

]
