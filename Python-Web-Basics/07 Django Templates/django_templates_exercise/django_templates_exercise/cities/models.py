from django.db import models


# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=15)
    city_population = models.IntegerField()
    city_image = models.ImageField(upload_to='media')

    # """ Initially I used method below to find picture dir."""
    # def image_dir(self):
    #     suffix = str(self.city_image).split('.')[-1]
    #     print(f"media/{self.city_name.lower()}.{suffix}")
    #     return f"media/{self.city_name.lower()}.{suffix}"

    def __str__(self):
        return f"{self.id}. {self.city_name} has {self.city_population} people! "
