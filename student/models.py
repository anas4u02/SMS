from django.db import models
from classes.models import ClassInfo
from teacher.models import Teacher 


class Student(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    class_details = models.ForeignKey(ClassInfo, on_delete=models.CASCADE,related_name="classinfo")
