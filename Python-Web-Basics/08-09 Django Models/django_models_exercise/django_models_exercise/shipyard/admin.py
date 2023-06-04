from django.contrib import admin

from django_models_exercise.shipyard.models import Worker, Department, WorkerAddress, ShipProject


# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ('first_name', 'last_name', 'experience', 'worker_age')
    list_filter = ['working_project', 'department']
    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name', 'worker_age'), 'birth_date', 'address')}),
        ('Working Info', {'fields': (('department', 'worker_rang'), ('experience',), 'working_project')}),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department_name',)}


@admin.register(WorkerAddress)
class WorkerAddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'country', 'street']
    prepopulated_fields = {'slug': ('city', 'country', 'street')}


@admin.register(ShipProject)
class AdminProject(admin.ModelAdmin):
    ...
