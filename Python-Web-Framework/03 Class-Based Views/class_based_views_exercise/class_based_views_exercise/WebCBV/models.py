from django.db import models


# Create your models here.
class Motorcycle(models.Model):
    brand = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    displacement = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    year = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.brand}: {self.model} -- {self.displacement}cc : {self.year}"
