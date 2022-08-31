from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from teacher.models import Teacher
from teacher.serializers import teacherSerializer, teacherSerializer2

class teacherOps(APIView):
    def get(self,request,pk):
        if pk =="0":
            teacher = Teacher.objects.all()
            serializer = teacherSerializer2(teacher,many=True)
            return Response(serializer.data)
        else:
            teacher = Teacher.objects.get(pk=pk)
            serializer = teacherSerializer2(teacher)
            return Response(serializer.data)
    
    def post(self,request):
        serializer = teacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk ):
        teacher = Teacher.objects.get(pk=pk)
        serializer =  teacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self,request,pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(data = "Succuesfully Deleted", status=status.HTTP_200_OK) 