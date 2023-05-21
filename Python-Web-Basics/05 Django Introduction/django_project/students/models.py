from django.db import models


# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    student_grade = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}: - {self.student_grade}"
