from django.core import validators
from my_plant_app_exam.web_plant.validators import upper_case_validator, only_letters_validator
from django.db import models


class Profile(models.Model):
    __MAX_LEN_USERNAME = 10
    __MIN_LEN_USERNAME = 2

    __MAX_LEN_OF_NAME = 20

    username = models.CharField(
        max_length=__MAX_LEN_USERNAME,
        null=False,
        blank=False,

        validators=(
            validators.MinLengthValidator(__MIN_LEN_USERNAME),
        )
    )

    first_name = models.CharField(
        max_length=__MAX_LEN_OF_NAME,
        null=False,
        blank=False,

        validators=(upper_case_validator,)
    )

    last_name = models.CharField(
        max_length=__MAX_LEN_OF_NAME,
        null=False,
        blank=False,

        validators=(upper_case_validator,)
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


def choices_menu():
    plants_types = ((t, t) for t in ["Outdoor Plants", "Indoor Plants"])
    return plants_types


class Plant(models.Model):
    __PLANT_TYPE_MAX_LEN = 14

    __NAME_MAX_LEN = 20
    __NAME_MIN_LEN = 2

    plant_type = models.CharField(
        max_length=__PLANT_TYPE_MAX_LEN,
        null=False,
        blank=False,
        choices=choices_menu(),
    )
    name = models.CharField(
        max_length=__NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(__NAME_MIN_LEN),
            only_letters_validator,
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
    price = models.FloatField(
        null=False,
        blank=False,
    )
