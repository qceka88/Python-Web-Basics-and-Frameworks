from django.contrib import admin

from django_templates_exercise.cities.models import City


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ...
