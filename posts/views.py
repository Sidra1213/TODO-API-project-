from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # 1. Yeh import karein
from django.shortcuts import get_object_or_404
from .serializers import TodoSerializer
from .models import Todo


class TodoView(APIView):
    def get(self,request):
        
        task=Todo.objects.filter(user=request.user).order_by("-created_at")
        
        serializer=TodoSerializer(task,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,todo_id):
        task=get_object_or_404(Todo,user=request.user,id=todo_id)
        serializer=TodoSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,todo_id):
        task=get_object_or_404(Todo,user=request.user,id=todo_id)
        task.delete
        
        return Response(
            {"massge":"todo is deleted motherfaucker"},
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
        

