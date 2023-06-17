from django.urls import path, include

from online_library.library_web.views import index, add_book_page, edit_book_page, details_book_page, profile_page, \
    profile_edit_page, profile_delete_page, delete_book

urlpatterns = [
    path('', index, name='home page'),
    path('add/', add_book_page, name='add book page'),
    path('edit/<int:pk>/', edit_book_page, name='edit book page'),
    path('details/<int:pk>/', details_book_page, name='details book page'),
    path('delete/<int:pk>/', delete_book, name = 'delete book'),
    path('profile/', include([
        path('', profile_page, name='profile page'),
        path('edit/', profile_edit_page, name='profile edit page'),
        path('delete/', profile_delete_page, name='profile delete page'),
    ])),
]
