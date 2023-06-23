from django.db import models
from django.core import validators
from home_work.WebHomeWork.validators import validate_username_characters


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            validate_username_characters,
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class AlbumModel(models.Model):
    GENRES_LIST = (
        "Pop Music", "Jazz Music", "R&B Music", "Rock Music",
        "Country Music", "Dance Music", "Hip Hop Music", "Other")
    GENRES_MENU = ((c, c) for c in GENRES_LIST)

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
    )
    artist = models.CharField(
        null=False,
        blank=False,
    )
    genre = models.CharField(
        null=False,
        blank=False,
        choices=GENRES_MENU,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        )
    )
