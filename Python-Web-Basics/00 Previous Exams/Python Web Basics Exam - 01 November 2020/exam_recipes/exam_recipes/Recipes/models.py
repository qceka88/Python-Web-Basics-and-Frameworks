from django.db import models


# Create your models here.
class Recipe(models.Model):
    MAX_TITLE_LEN = 30
    MAX_LEN_INGREDIENTS = 250

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TITLE_LEN,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    ingredients = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_INGREDIENTS,

    )
    recipe_time = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
