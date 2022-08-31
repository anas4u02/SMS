from dataclasses import fields
from rest_framework import serializers
import classes

from classes.serializers import ClassSerializer
from teacher.serializers import teacherSerializer
from .models import Student
from classes.models import ClassInfo
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["fname","lname"]

class ClassSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(source ="teacher_set",many=True)
    class Meta:
        model = ClassInfo
        # fields = ["name","size","div"]
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class_details = serializers.CharField(source = "class_details.name")
    # class_details = ClassSerializer()
    class Meta:
        model = Student
        # fields= ["fname","lname","gender","classinfo"]
        fields= '__all__'

class StudentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields= ['fname','lname','gender','class_details']