from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from .models import Teacher,Subject,AdminLogin,TeacherLogin,TeacherSelection,ClassDivisions
from .serializers import Teacherserializer,Subjectserializer,AdminLoginserializer,TeacherLoginserializer
from .serializers import TeacherSelectionserializer,ClassDivisionsserializer 
class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class =Subjectserializer

class AdminLoginView(generics.ListCreateAPIView):
    queryset = AdminLogin.objects.all()
    serializer_class =AdminLoginserializer

class TeacherLoginView(generics.ListCreateAPIView):
    queryset = TeacherLogin.objects.all()
    serializer_class =TeacherLoginserializer

class TeacherDeletion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()
class TeacherUpdation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()

class TeacherSelectionview(generics.ListCreateAPIView):
    queryset = TeacherSelection.objects.all()
    serializer_class =TeacherSelectionserializer

class ClassDivisionsview(generics.ListCreateAPIView):
    queryset = ClassDivisions.objects.all()
    serializer_class =ClassDivisionsserializer

