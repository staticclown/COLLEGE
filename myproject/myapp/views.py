from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from .models import Teacher
from .serializers import Teacherserializer

class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer