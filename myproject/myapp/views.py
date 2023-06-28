from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,QueryDict
from rest_framework import generics
from .models import Teacher,Subject,AdminLogin,TeacherLogin,TeacherSelection,ClassDivisions
from .models import Department,Phase,phaseno
from .serializers import Teacherserializer,Subjectserializer,AdminLoginserializer,TeacherLoginserializer
from .serializers import TeacherSelectionserializer,ClassDivisionsserializer ,Departmentserializer,Phaseserializer
from .serializers import Phasenoserializer
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

class phase1view(generics.ListCreateAPIView):
    serializer_class = Phasenoserializer
    queryset=phaseno.objects.all()
    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        title =requestbody['no']
        a=requestbody['active']
        new_start=phaseno(no=title[0],active=a[0])


        p=Teacher.objects.all()
        arrtid=[]
        arrexp=[]
        arrmail=[]
        for i in p:
            arrtid.append(i.tid)
            val=2023-int(i.year.strftime('%Y'))
            arrexp.append(val)
            arrmail.append(i.tmail)
        count=len(arrexp)
        for i in range(count-1):
            for j in range(count-i-1):
                if arrexp[j]>arrexp[j+1]:
                    arrexp[j],arrexp[j+1]=arrexp[j+1],arrexp[j]
                    arrtid[j],arrtid[j+1]=arrtid[j+1],arrtid[j]
                    arrmail[j],arrmail[j+1]=arrmail[j+1],arrmail[j]

        count=count//3
        for k in range(count):
            val=arrtid[k]
            obj=Teacher.objects.get(tid=val)
            new_entry=Phase(no=1,tid=obj,alloc=0,status='ON',exp=arrexp[k],sub1='',sub2='',lab1='',lab2='',academicyear=title[0],mail=arrmail[k])
            new_entry.save() 
        return HttpResponse('OK',status=status.HTTP_200_OK)


class phase2view(generics.ListCreateAPIView):
    serializer_class = Phasenoserializer
    queryset =phaseno.objects.all()
    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        title =requestbody['no']
        p=Teacher.objects.all()
        arrtid=[]
        arrexp=[]
        arrmail=[]
        for i in p:
            arrtid.append(i.tid)
            val=2023-int(i.year.strftime('%Y'))
            arrexp.append(val)
            arrmail.append(i.tmail)
        count=len(arrexp)
        for i in range(count-1):
            for j in range(count-i-1):
                if arrexp[j]>arrexp[j+1]:
                    arrexp[j],arrexp[j+1]=arrexp[j+1],arrexp[j]
                    arrtid[j],arrtid[j+1]=arrtid[j+1],arrtid[j]
                    arrmail[j],arrmail[j+1]=arrmail[j+1],arrmail[j]

        c=Phase.objects.all()
        count=len(p)-len(c)
        k=len(c)-1
        print(k,count)
        while k<count:
            val=arrtid[k]
            obj=Teacher.objects.get(tid=val)
            new_entry=Phase(no=2,tid=obj,alloc=0,status='ON',exp=arrexp[k],sub1='',sub2='',lab1='',lab2='',academicyear=title[0],mail=arrmail[k])
            new_entry.save()
            k=k+1
        return HttpResponse('OK',status=status.HTTP_200_OK)

class phasestatusview(generics.ListCreateAPIView):
    queryset = phaseno.objects.all()
    serializer_class =Phasenoserializer

