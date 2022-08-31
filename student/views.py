from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classes.models import ClassInfo
from student.serializers import StudentSerializer,StudentSerializer2 
from .serializers import *
from student.models import Student
from teacher.models import Teacher
from teacher.serializers import teacherSerializer

class studentOps(APIView):
    def get(self,request,pk):
        if pk =="0":
            student = Student.objects.all()
            teacher = Teacher.objects.all()
            serializer = StudentSerializer2(student,many=True)
            serializer2 = teacherSerializer(teacher,many=True)
            return Response({'student':serializer.data, 'teacher':serializer2.data})
        else:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer2(student)
            return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk):
        student = Student.objects.get(pk=pk)
        serializer =  StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self,request,pk):
        teacher = Student.objects.get(pk=pk)
        teacher.delete()
        return Response(data = "Succuesfully Deleted", status=status.HTTP_200_OK) 


class ClassView(APIView):
    def get(self,request,*args, **kwargs):
        return Response (data =StudentSerializer(Student.objects.all(),many=True).data)