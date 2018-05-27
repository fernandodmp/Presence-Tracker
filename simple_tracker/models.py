from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 50, unique=True, primary_key = True)
    misses = models.IntegerField(default=0)

    def __str__(self):
        return self.name



