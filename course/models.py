from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Courses(models.Model):
    courseName = models.CharField(max_length=50,unique=True)
    courseFee = models.IntegerField()
    courseDuration = models.CharField(max_length=50)

class Signup(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
