from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from .models import Teacher,Subject,AdminLogin,TeacherLogin,TeacherSelection,ClassDivisions
from .serializers import Teacherserializer,Subjectserializer,AdminLoginserializer,TeacherLoginserializer
from .serializers import TeacherSelectionserializer,ClassDivisionsserializer 
from rest_framework.response import Response
#from rest_framework import APIView
from rest_framework import status
class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class =Subjectserializer

class AdminLoginView(generics.CreateAPIView):
    serializer_class =AdminLoginserializer
    def post(self, request, *args, **kwargs):
        title = request.POST.get('aid')
        word=request.POST.get('password')
        print(word)
        if(word=='1234'):
            return Response('SUCCESS',status=status.HTTP_200_OK)
        else:
            return Response('NO',status=status.HTTP_200_OK)




class TeacherLoginView(generics.CreateAPIView):
    serializer_class =TeacherLoginserializer
    def post(self, request, *args, **kwargs):
        title = request.POST.get('Tid')
        word=request.POST.get('password')
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

