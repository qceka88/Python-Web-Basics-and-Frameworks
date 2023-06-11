from django.db import models

from car_collection_app_exam.car_collection.validators import min_len_username_validations, valid_year_check
from django.core import validators


# Create your models here.
class Profile(models.Model):
    __MAX_LEN_USERNAME = 10
    __MIN_AGE = 18
    __MAX_LEN_PASSWORD = 30
    __MAX_LEN_NAME = 30

    username = models.CharField(
        null=False,
        blank=False,
        max_length=__MAX_LEN_USERNAME,
        validators=(
            min_len_username_validations,
        ),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(__MIN_AGE),
        ),
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=__MAX_LEN_PASSWORD,

    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=__MAX_LEN_NAME
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=__MAX_LEN_NAME,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


def choices_menu():
    return ((o, o) for o in ["Sports Car", "Pickup", "Crossover", "Minibus", "Other"])


class Car(models.Model):
    __MAX_LEN_TYPE = 10
    __MAX_LEN_MODEL = 20
    __MIN_LEN_MODEL = 2
    __MIN_PRICE = 1

    car_type = models.CharField(
        null=False,
        blank=False,
        max_length=__MAX_LEN_TYPE,
        choices=choices_menu(),
    )
    car_model = models.CharField(
        null=False,
        blank=False,
        max_length=__MAX_LEN_MODEL,
        validators=(
            validators.MinLengthValidator(__MIN_LEN_MODEL),
        )
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            valid_year_check,
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(__MIN_PRICE),
        ),
    )
