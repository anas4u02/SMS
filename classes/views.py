from ast import Delete
from django.shortcuts import render
from .models import ClassInfo
from rest_framework.views import APIView
from .serializers import ClassSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ClassView(APIView):
    def get(self,request,pk):
        if pk == "0":
            classes = ClassInfo.objects.all()
            serializer = ClassSerializer(classes,many = True)
            return Response(serializer.data)
        else:
            classes= ClassInfo.objects.get(pk=pk)
            serializer = ClassSerializer(classes)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk):
        classes = ClassInfo.objects.get(pk=pk)
        serializer = ClassSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        classes = ClassInfo.objects.get(pk=pk)
        classes.delete()
        return Response(data="Class deleted succesfully!", status=status.HTTP_202_ACCEPTED)
