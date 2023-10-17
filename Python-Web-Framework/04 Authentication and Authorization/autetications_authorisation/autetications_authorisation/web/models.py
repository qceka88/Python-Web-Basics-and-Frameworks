from django.db import models


# Create your models here.
class Article(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    title = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
