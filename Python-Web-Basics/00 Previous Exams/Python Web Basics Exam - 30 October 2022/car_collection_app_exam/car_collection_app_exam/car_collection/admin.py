from django.contrib import admin

from car_collection_app_exam.car_collection.models import Profile, Car


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...
