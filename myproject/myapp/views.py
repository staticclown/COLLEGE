from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,QueryDict
from rest_framework import generics
from .models import Teacher,Subject,AdminLogin,TeacherLogin,TeacherSelection,ClassDivisions,Department
from .serializers import Teacherserializer,Subjectserializer,AdminLoginserializer,TeacherLoginserializer
from .serializers import TeacherSelectionserializer,ClassDivisionsserializer ,Departmentserializer
from rest_framework.response import Response
#from rest_framework import APIView
from rest_framework import status
from urllib.parse import urlparse
from urllib.parse import parse_qsl
import json
class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class =Subjectserializer

class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class =Departmentserializer

class AdminLoginView(generics.CreateAPIView):
    serializer_class =AdminLoginserializer
    
    def post(self, request, *args, **kwargs):
        #title = request.POST.get('aid')
        requestbody=dict(request.data)
        
        word=requestbody['password']
        if(word=='1234'):
            return Response('SUCCESS',status=status.HTTP_200_OK)
        else:
            return Response('NO',status=status.HTTP_200_OK)




class TeacherLoginView(generics.CreateAPIView):
    serializer_class =TeacherLoginserializer
    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        title =requestbody['Tid']
        word=requestbody['password']
        obj=Teacher.objects.get(tid=title)
        a1=obj.password
        a2=obj.tid
      
        if(word==a1):
            return Response('SUCCESS',status=status.HTTP_200_OK)
        else:
            return Response('NO',status=status.HTTP_200_OK)

class TeacherDeletion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()
class TeacherUpdation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()

class SubjectUpdation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Subjectserializer
    queryset = Subject.objects.all()

class TeacherSelectionview(generics.ListCreateAPIView):
    queryset = TeacherSelection.objects.all()
    serializer_class =TeacherSelectionserializer

class ClassDivisionsview(generics.ListCreateAPIView):
    queryset = ClassDivisions.objects.all()
    serializer_class =ClassDivisionsserializer

