from django.db import models

# Create your models here.

class Student(models.Model):
    No = models.IntegerField()
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Mobile_No = models.IntegerField()