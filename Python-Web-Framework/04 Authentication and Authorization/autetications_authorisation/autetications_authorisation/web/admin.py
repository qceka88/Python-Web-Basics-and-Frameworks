from django.contrib import admin

from autetications_authorisation_lab.web.models import Article


# Register your models here.
@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    ...
