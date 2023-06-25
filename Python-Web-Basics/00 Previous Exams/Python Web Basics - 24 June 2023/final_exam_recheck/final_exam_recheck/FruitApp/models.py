from django.db import models
from django.core import validators
from final_exam_recheck.FruitApp.validators import validate_fruit_name


# Create your models here.
class FruitModel(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[
            validators.MinLengthValidator(2),
            validate_fruit_name,
        ],
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True
    )
