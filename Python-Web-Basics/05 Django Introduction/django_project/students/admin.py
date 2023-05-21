from django.contrib import admin
from django_project.students.models import Students


@admin.register(Students)
class AdminStudent(admin.ModelAdmin):
    ...
