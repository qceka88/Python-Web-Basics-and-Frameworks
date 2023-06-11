from django.contrib import admin

from my_plant_app_exam.web_plant.models import Profile, Plant


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    ...