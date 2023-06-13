from django.contrib import admin

from games_play_app.GamesPlayApp.models import Profile, GameModel


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(GameModel)
class GameAdmin(admin.ModelAdmin):
    ...


