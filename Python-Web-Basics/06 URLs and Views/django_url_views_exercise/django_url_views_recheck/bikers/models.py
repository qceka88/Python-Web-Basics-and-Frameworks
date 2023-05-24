from django.db import models


# Create your models here.

class Bikers(models.Model):
    biker_name = models.CharField(max_length=30)
    bike_brand = models.CharField(max_length=30)
    bike_volume = models.IntegerField()
    biker_city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}:  Name: {self.biker_name},  Brand: {self.bike_brand},  CC: {self.bike_volume} from {self.biker_city}."
