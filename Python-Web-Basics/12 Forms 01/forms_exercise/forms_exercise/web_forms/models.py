from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    password = models.CharField(
        max_length=50,
        editable=True,
    )

    def __str__(self):
        return f"{self.name} {self.age}"
