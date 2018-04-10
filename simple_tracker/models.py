from django.db import models
from django.forms import ModelForm

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 50, unique=True, primary_key = True)
    misses = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
