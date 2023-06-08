from django.db import models
from django.core import exceptions, validators


# Create your models here.
def validate_username(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    __USERNAME_MAX_LEN = 15
    __USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=__USERNAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(__USERNAME_MIN_LEN),
            validate_username,
        )

    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )


def choices_menu():
    genres_list = ["Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music",
                   "Hip Hop Music" "Other"]
    list_of_choices = [(m, m) for m in genres_list]
    return list_of_choices


class Album(models.Model):
    __MAX_ALBUM_NAME_LEN = 30
    __MAX_ARTIST_NAME_LEN = 30
    __MAX_GENRE_NAME_LEN = 30

    album_name = models.CharField(
        unique=True,
        max_length=__MAX_ALBUM_NAME_LEN,
        null=False,
        blank=False,
    )
    artist = models.CharField(
        max_length=__MAX_ARTIST_NAME_LEN,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=__MAX_GENRE_NAME_LEN,
        null=False,
        blank=False,
        choices=choices_menu()

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

        validators=(validators.MinValueValidator(0.0),)

    )
