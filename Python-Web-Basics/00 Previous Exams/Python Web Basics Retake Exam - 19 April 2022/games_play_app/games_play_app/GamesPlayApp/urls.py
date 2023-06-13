from django.urls import path, include

from games_play_app.GamesPlayApp.views import index, profile_create, dashboard_view, game_create, game_details, \
    game_edit, game_delete, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', index, name='home page'),
    path('dashboard/', dashboard_view, name='dashboard page'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('game/', include([
        path('create/', game_create, name='game create'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', game_edit, name='game edit'),
        path('delete/<int:pk>/', game_delete, name='game delete'),
    ])),

]
