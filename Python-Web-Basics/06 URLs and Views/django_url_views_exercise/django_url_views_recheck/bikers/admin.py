from django.contrib import admin
from django_url_views_recheck.bikers.models import Bikers


# Register your models here.

@admin.register(Bikers)
class BikerAdmin(admin.ModelAdmin):
    ...
