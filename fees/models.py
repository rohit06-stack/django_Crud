from django.db import models

# Create your models here.
class Fees(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.IntegerField()

    def __str__(self) -> str:
        return self.name