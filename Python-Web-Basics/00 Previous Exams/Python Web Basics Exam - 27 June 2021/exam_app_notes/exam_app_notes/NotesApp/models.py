from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_LEN_NAME = 20

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_NAME,
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_NAME,
    )

    age = models.IntegerField(
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )


class Note(models.Model):
    MAX_TITLE_LEN = 30

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TITLE_LEN,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )
