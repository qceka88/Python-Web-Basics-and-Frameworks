from django.db import models


# Create your models here.
class Profile(models.Model):
    NAME_MAX_LEN = 30

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LEN,
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LEN
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )


class Book(models.Model):
    TITLE_MAX_LEN = 30
    TYPE_MAX_LEN = 30

    title = models.CharField(
        null=False,
        blank=False,
        max_length=TITLE_MAX_LEN,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    book_type = models.CharField(
        null=False,
        blank=False,
        max_length=TYPE_MAX_LEN,
    )
