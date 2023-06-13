from django.core import validators
from django.db import models


# Create your models here.
class Profile(models.Model):
    MINIMUM_AGE = 12
    PASSWORD_MAX_LEN = 30
    NAMES_MAX_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MINIMUM_AGE),
        )
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LEN,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=NAMES_MAX_LEN,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=NAMES_MAX_LEN,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


def choices_menu():
    menu = ["Action", "Adventure", "Puzzle", "Strategy", "Sports", "Board/Card Game", "Other"]
    return ((option, option) for option in menu)


class GameModel(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    LEVEL_MAX_MIN_VALUE = 1

    title = models.CharField(
        null=False,
        blank=False,
        max_length=TITLE_MAX_LEN,
        unique=True,
    )
    category = models.CharField(
        null=False,
        blank=False,
        max_length=CATEGORY_MAX_LEN,
        choices=choices_menu(),

    )
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_RATING),
            validators.MaxValueValidator(MAX_RATING),
        )
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(LEVEL_MAX_MIN_VALUE),
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
