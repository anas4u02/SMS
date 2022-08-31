from django.db import models


class ClassInfo(models.Model):
    name = models.CharField(max_length=5)
    size = models.IntegerField()
    div = models.CharField(max_length=2)