from django.urls import path, include

from home_work.WebHomeWork.views import index, album_add_page, details_album_page, edit_album_page, delete_album_page, \
    profile_details_page, profile_delete_page

urlpatterns = (
    path('', index, name='home page'),
    path('album/', include([
        path('add/', album_add_page, name='album add page'),
        path('details/<int:id>/', details_album_page, name='details album page'),
        path('edit/<int:id>/', edit_album_page, name='edit album page'),
        path('delete/<int:id>/', delete_album_page, name='delete album page'),
    ])),
    path('profile/', include([
        path('details/', profile_details_page, name='profile details page'),
        path('delete/', profile_delete_page, name='profile delete page'),
    ])),
)
