from dataclasses import fields
import imp
from rest_framework import serializers
from .models import ClassInfo

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInfo
        fields = "__all__"