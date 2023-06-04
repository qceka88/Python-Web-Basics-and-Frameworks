from django.db import models


def choices_menu():
    LEVEL_BEGINNER = 'BEGINNER'
    LEVEL_NORMAL = 'NORMAL'
    LEVEL_SENIOR = 'SENIOR'
    LEVEL_SUPERVISOR = 'SUPERVISOR'
    LEVEL_MANAGER = 'PRODUCTION MANAGER'

    LEVELS_MENU = [
        ('BEG', LEVEL_BEGINNER),
        ('NOR', LEVEL_NORMAL),
        ('SEN', LEVEL_SENIOR),
        ('SUP', LEVEL_SUPERVISOR),
        ('MAN', LEVEL_MANAGER),
    ]

    return LEVELS_MENU


# Create your models here.
class Worker(models.Model):
    class Meta:
        ordering = ['first_name']

    first_name = models.CharField(max_length=30, blank=False, default='first name')
    last_name = models.CharField(max_length=30, blank=False, default='last name')

    worker_age = models.IntegerField()
    birth_date = models.DateField()

    experience = models.PositiveIntegerField()

    worker_rang = models.CharField(max_length=30, choices=choices_menu())

    start_work = models.DateTimeField(auto_now_add=True)
    update_status = models.DateTimeField(auto_now=True)

    department = models.ManyToManyField(to='Department')

    address = models.OneToOneField(to='WorkerAddress', on_delete=models.CASCADE, null=True, blank=True, max_length=100)

    working_project = models.ManyToManyField(to='ShipProject')

    @property
    def worker_data(self):
        return f"{self.first_name} {self.last_name} - {self.worker_age}"

    def __str__(self):
        return f"{self.pk}: {self.worker_data}. Work as {str(self.department.get()).lower()}!"


class Department(models.Model):
    department_name = models.CharField(max_length=35)
    slug = models.SlugField(unique=True, max_length=100)

    @property
    def department_data(self):
        return f"{self.pk}: {self.department_name}"

    def __str__(self):
        return f"{self.department_name}"


class WorkerAddress(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.TextField()

    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}, st.{self.street}"


class ShipProject(models.Model):
    ship_type = models.CharField(max_length=30)
    ship_name = models.CharField(max_length=30)
    ship_length = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ship_name}, type:{self.ship_type}, length: {self.ship_length}!"
