from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Book(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
