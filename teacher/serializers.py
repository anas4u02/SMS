from rest_framework import serializers
from .models import Teacher
from classes.serializers import ClassSerializer

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class teacherSerializer2(serializers.ModelSerializer):
    teaches = ClassSerializer()
    class Meta:
        model = Teacher
        fields = ['fname','lname','subject','teaches']