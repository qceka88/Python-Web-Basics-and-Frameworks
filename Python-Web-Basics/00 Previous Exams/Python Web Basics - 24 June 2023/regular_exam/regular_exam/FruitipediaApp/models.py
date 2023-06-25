from django.db import models
from django.core import validators
from .validators import validate_profile_name_first_letter, validate_fruit_name


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(
            validators.MinLengthValidator(2),
            validate_profile_name_first_letter,
        )
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=(
            validators.MinLengthValidator(1),
            validate_profile_name_first_letter,
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            validators.MinLengthValidator(8),
        )
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )


class FruitModel(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_fruit_name,
        )
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
        blank=True,

    )

