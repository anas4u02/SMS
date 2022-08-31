from django.db import models
from classes.models import ClassInfo 

class Teacher(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    teaches = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)