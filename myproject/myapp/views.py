from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,QueryDict
from rest_framework import generics
from .models import Teacher,Subject,AdminLogin,TeacherLogin,TeacherSelection,ClassDivisions
from .models import Department,phaseno,Phase
from .serializers import Teacherserializer,Subjectserializer,AdminLoginserializer,TeacherLoginserializer
from .serializers import TeacherSelectionserializer,Departmentserializer,Phaseserializer
from .serializers import Phasenoserializer,ClassDivisionsserializer,Addclassserializer
from rest_framework.response import Response
#from rest_framework import APIView
from rest_framework import status
from urllib.parse import urlparse
from urllib.parse import parse_qsl
import json
import random
from datetime import date

class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class =Subjectserializer

class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class =Departmentserializer

class phaseview(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class =Phaseserializer

    
class DepartmentUpdation(generics.RetrieveUpdateDestroyAPIView):
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

class Phaseview(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class =Phaseserializer

class Phaseupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phase.objects.all()
    serializer_class =Phaseserializer
    
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

class split(generics.CreateAPIView):
    #queryset = Subject.objects.all()
    serializer_class =Subjectserializer

    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        print(requestbody)
        sid=requestbody['subid']
        subname=requestbody['subname']
        sem=requestbody['sem']
        did=requestbody['depid']
        subtype=requestbody['subtype']
        user=Department.objects.get(depid=did)
        sub=Subject.objects.get(subid=sid)
        i=0
        count=user.division
      
        name=user.depname
        
        while i<count:
            if subtype=='T':
                no=random.randint(10000,99999)
                no='C'+str(no)
                print(no)
                new_entry=ClassDivisions(classid=no,classname=name+'-'+chr(i+ord('A')),subject=sub,depid=user,classalloc=0,exp=0,
                sem=sem,subtype=subtype)
                new_entry.save()
               
            elif subtype=='L':
                k=0
                while k<3:
                    no=random.randint(10000,99999)
                    no='C'+str(no)
                    print(no)
                    new_entry=ClassDivisions(classid=no,classname=name+'-'+chr(i+ord('A')),subject=sub,depid=user,classalloc=0,exp=0,
                    sem=sem,subtype=subtype)
                    new_entry.save()
                    k=k+1
            i=i+1
            
        return HttpResponse('OK',status=status.HTTP_200_OK)
class phase1view(generics.ListCreateAPIView):
    serializer_class = Phasenoserializer
    queryset=phaseno.objects.all()
    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        Phase.objects.all().delete()
        phaseno.objects.all().delete()
        title =requestbody['no']
        a=requestbody['active']
        
        new_start=phaseno(no=title,active=a)
        new_start.save()
        p=Teacher.objects.all()
        arrtid=[]
        arrexp=[]
        arrmail=[]
        for i in p:
            arrtid.append(i.tid)
            current_year = date.today().year
            val=current_year-int(i.year.strftime('%Y'))
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
            no=random.randint(10000,99999)
            no='P'+str(no)
            obj=Teacher.objects.get(tid=val)
            new_entry=Phase(no=1,pid=no,tid=obj,alloc=0,status='ON',exp=arrexp[k],sub1='',sub2='',sub3='',sub4='',sub5='',
            sub6='',academicyear=title,mail=arrmail[k])
            new_entry.save() 
        return HttpResponse('OK',status=status.HTTP_200_OK)


class phase2view(generics.ListCreateAPIView):
    serializer_class = Phasenoserializer
    queryset =phaseno.objects.all()
    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        phaseno.objects.all().delete()
       
        title =requestbody['no']
        a=requestbody['active']
        new_start=phaseno(no=title,active=a)
        new_start.save()
        p=Teacher.objects.all()
        arrtid=[]
        arrexp=[]
        arrmail=[]
        for i in p:
            arrtid.append(i.tid)
            current_year = date.today().year
            val=current_year-int(i.year.strftime('%Y'))
            arrexp.append(val)
            arrmail.append(i.tmail)
        count=len(arrexp)-1
        for i in range(count-1):
            for j in range(count-i-1):
                if arrexp[j]>arrexp[j+1]:
                    arrexp[j],arrexp[j+1]=arrexp[j+1],arrexp[j]
                    arrtid[j],arrtid[j+1]=arrtid[j+1],arrtid[j]
                    arrmail[j],arrmail[j+1]=arrmail[j+1],arrmail[j]

        c=Phase.objects.all()
       
        count=len(p)-len(c)
        k=len(c)
        Phase.objects.all().delete()
        print(k,count)
        print(arrtid)
        
        while k<=count:
            val=arrtid[k]
            no=random.randint(10000,99999)
            no='P'+str(no)
            obj=Teacher.objects.get(tid=val)
            new_entry=Phase(no=2,pid=no,tid=obj,alloc=0,status='ON',exp=arrexp[k],sub1='',sub2='',sub3='',sub4=''
            ,sub5='',sub6='',academicyear=title,mail=arrmail[k])
            new_entry.save()
            k=k+1
        return HttpResponse('OK',status=status.HTTP_200_OK)

class phasestatusview(generics.ListCreateAPIView):
    queryset = phaseno.objects.all()
    serializer_class =Phasenoserializer

class subselect(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class =Addclassserializer
    def post(self, request, *args, **kwargs):
        requestbody=dict(request.data)
        tid =requestbody['tid']
        count=requestbody['no']
        sub1=requestbody['sub1']
        sub2=requestbody['sub2']
        sub3=requestbody['sub3']
        sub4=requestbody['sub4']
        sub5=requestbody['sub5']
        sub6=requestbody['sub6']
        year=requestbody['academicyear']
        phaseid=Phase.objects.get(tid=tid)
        phaseid.no=count
        phaseid.sub1=sub1
        phaseid.sub2=sub2
        phaseid.sub3=sub3
        phaseid.sub4=sub4
        phaseid.sub5=sub5
        phaseid.sub6=sub6
        phaseid.academicyear=year
        teacherid=Teacher.objects.get(tid=tid)
        phaseid.mail=teacherid.tmail
        phaseid.status="OFF"
        phaseid.save()

        return HttpResponse('OK',status=status.HTTP_200_OK)

