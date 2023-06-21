from django.shortcuts import render
from django.http import HttpResponse
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
class TeacherDeletion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()

    # Permission_classes = [IsAuthenticated]
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method != 'GET':
    #         permission_classes = [IsAuthenticated]

    #     return [permission() for permission in permission_classes]
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('new response')

def fun1(request,pk):
    obj=Teacher.objects.get(pk)
    if(request.method=='POST'):
        obj.delete()

