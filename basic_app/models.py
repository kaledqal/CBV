from django.db import models
from django.urls import reverse,reverse_lazy

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the school """
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:school_detail',kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        """returns a string representation of the student """
        return self.name
