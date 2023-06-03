from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from .models import Teacher,Subject,Login
from .serializers import Teacherserializer,Subjectserializer,Loginserializer

class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class =Subjectserializer

class LoginView(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class =Loginserializer
