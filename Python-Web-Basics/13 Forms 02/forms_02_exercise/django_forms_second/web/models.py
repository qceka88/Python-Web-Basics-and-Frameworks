from django.db import models

from django_forms_second.web.validators import ValueInRangeValidator


# Create your models here.

class TodoModel(models.Model):
    text = models.CharField(max_length=100,
                            error_messages={
                                "unique": "The name is already taken."
                            },
                            unique=True
                            )

    done = models.BooleanField(default=False)
    priority = models.IntegerField(
        validators=[
            ValueInRangeValidator(6, 8),
        ]
    )

    def __str__(self):
        return f"{self.text} - {self.priority}"


class ImageModel(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    description = models.CharField(blank=True, null=True, max_length=100)
