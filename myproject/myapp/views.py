from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, QueryDict
from rest_framework import generics
from .models import (
    Teacher,
    Subject,
    AdminLogin,
    TeacherLogin,
    TeacherSelection,
    ClassDivisions,
    Final,
    otherSubject,
)
from .models import Department, phaseno, Phase,clash
from .serializers import (
    Teacherserializer,
    Subjectserializer,
    AdminLoginserializer,
    TeacherLoginserializer,
    Finalserializer,
    otherSubjectserializer,
)
from .serializers import (
    TeacherSelectionserializer,
    Departmentserializer,
    Phaseserializer,
    clashserializer
)
from .serializers import Phasenoserializer, ClassDivisionsserializer, Addclassserializer
from rest_framework.response import Response

# from rest_framework import APIView
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
    serializer_class = Subjectserializer


class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = Departmentserializer


class phaseview(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class = Phaseserializer


class DepartmentUpdation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = Departmentserializer


class AdminLoginView(generics.CreateAPIView):
    serializer_class = AdminLoginserializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)

        word = requestbody["password"]
        if word == "1234":
            return Response("SUCCESS", status=status.HTTP_200_OK)
        else:
            return Response("NO", status=status.HTTP_200_OK)


class Phaseview(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class = Phaseserializer


class Phaseupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phase.objects.all()
    serializer_class = Phaseserializer


class TeacherLoginView(generics.CreateAPIView):
    serializer_class = TeacherLoginserializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        title = requestbody["Tid"]
        word = requestbody["password"]
        obj = Teacher.objects.get(tid=title)
        a1 = obj.password
        a2 = obj.tid

        if word == a1:
            return Response("SUCCESS", status=status.HTTP_200_OK)
        else:
            return Response("NO", status=status.HTTP_200_OK)


class TeacherDeletion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()


class TeacherUpdation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()


class SubjectUpdation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Subjectserializer
    queryset = Subject.objects.all()



class ClassDivisionsview(generics.ListCreateAPIView):
    queryset = ClassDivisions.objects.all()
    serializer_class = ClassDivisionsserializer


class split(generics.CreateAPIView):
    # queryset = Subject.objects.all()
    serializer_class = Subjectserializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        print(requestbody)
        sid = requestbody["subid"]
        subname = requestbody["subname"]
        sem = requestbody["sem"]
        did = requestbody["depid"]
        subtype = requestbody["subtype"]
        user = Department.objects.get(depid=did)
        sub = Subject.objects.get(subid=sid)
        i = 0
        count = user.division

        name = user.depname

        while i < count:
            if subtype == "T":
                no = random.randint(10000, 99999)
                no = "C" + str(no)
                print(no)
                new_entry = ClassDivisions(
                    classid=no,
                    classname=name + "-" + chr(i + ord("A")),
                    subject=sub,
                    depid=user,
                    classalloc=0,
                    exp=0,
                    sem=sem,
                    subtype=subtype,
                )
                new_entry.save()

            elif subtype == "L":
                k = 0
                while k < 3:
                    no = random.randint(10000, 99999)
                    no = "C" + str(no)
                    print(no)
                    new_entry = ClassDivisions(
                        classid=no,
                        classname=name + "-" + chr(i + ord("A")),
                        subject=sub,
                        depid=user,
                        classalloc=0,
                        exp=0,
                        sem=sem,
                        subtype=subtype,
                    )
                    new_entry.save()
                    k = k + 1
            i = i + 1

        return HttpResponse("OK", status=status.HTTP_200_OK)


class othersplitview(generics.CreateAPIView):
    serializer_class = otherSubjectserializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        print(requestbody)
        sid = requestbody["subid"]
        subname = requestbody["subname"]
        sem = requestbody["sem"]
        did = requestbody["depid"]
        subtype = requestbody["subtype"]
        count=requestbody['count']
        user = Department.objects.get(depid=did)
        sub = Subject.objects.get(subid=sid)
        name = user.depname

        i=0

        while i<count:
            
                if subtype == "E" or "H" or "M":
                    no = random.randint(10000, 99999)
                    no = "C" + str(no)
                    print(no)
                    new_entry = ClassDivisions(
                        classid=no,
                        classname=name ,
                        subject=sub,
                        depid=user,
                        classalloc=0,
                        exp=0,
                        sem=sem,
                        subtype=subtype,
                    )
                    new_entry.save()
                
                

                i=i+1
        return HttpResponse("OK", status=status.HTTP_200_OK)



class phase1view(generics.ListCreateAPIView):
    serializer_class = Phasenoserializer
    queryset = phaseno.objects.all()

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        Phase.objects.all().delete()
        phaseno.objects.all().delete()
        title = requestbody["no"]
        a = requestbody["active"]

        new_start = phaseno(no=title, active=a)
        new_start.save()
        p = Teacher.objects.all()
        arrtid = []
        arrexp = []
        arrmail = []
        for i in p:
            arrtid.append(i.tid)
            current_year = date.today().year
            val = current_year - int(i.year.strftime("%Y"))
            arrexp.append(val)
            arrmail.append(i.tmail)
        count = len(arrexp)
        for i in range(count - 1):
            for j in range(count - i - 1):
                if arrexp[j] < arrexp[j + 1]:
                    arrexp[j], arrexp[j + 1] = arrexp[j + 1], arrexp[j]
                    arrtid[j], arrtid[j + 1] = arrtid[j + 1], arrtid[j]
                    arrmail[j], arrmail[j + 1] = arrmail[j + 1], arrmail[j]

        count = count // 3
        for k in range(count):
            val = arrtid[k]
            no = random.randint(10000, 99999)
            no = "P" + str(no)
            obj = Teacher.objects.get(tid=val)
            new_entry = Phase(
                no=0,
                pid=no,
                tid=obj,
                alloc=0,
                status="ON",
                exp=arrexp[k],
                sub1="",
                sub2="",
                sub3="",
                sub4="",
                sub5="",
                sub6="",
                academicyear=title,
                mail=arrmail[k],
            )
            new_entry.save()
        return HttpResponse("OK", status=status.HTTP_200_OK)


class phase2view(generics.ListCreateAPIView):
    serializer_class = Phasenoserializer
    queryset = phaseno.objects.all()

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        phaseno.objects.all().delete()

        title = requestbody["no"]
        a = requestbody["active"]
        new_start = phaseno(no=title, active=a)
        new_start.save()
        p = Teacher.objects.all()
        arrtid = []
        arrexp = []
        arrmail = []
        for i in p:
            arrtid.append(i.tid)
            current_year = date.today().year
            val = current_year - int(i.year.strftime("%Y"))
            arrexp.append(val)
            arrmail.append(i.tmail)
        count = len(arrexp) - 1
        for i in range(count - 1):
            for j in range(count - i - 1):
                if arrexp[j] < arrexp[j + 1]:
                    arrexp[j], arrexp[j + 1] = arrexp[j + 1], arrexp[j]
                    arrtid[j], arrtid[j + 1] = arrtid[j + 1], arrtid[j]
                    arrmail[j], arrmail[j + 1] = arrmail[j + 1], arrmail[j]

        c = Phase.objects.all()

        count = len(p) - len(c)
        k = len(c) - 1
        Phase.objects.all().delete()
        print(k, count)
        print(arrtid)

        while k <= count:
            val = arrtid[k]
            no = random.randint(10000, 99999)
            no = "P" + str(no)
            obj = Teacher.objects.get(tid=val)
            new_entry = Phase(
                no=0,
                pid=no,
                tid=obj,
                alloc=0,
                status="ON",
                exp=arrexp[k],
                sub1="",
                sub2="",
                sub3="",
                sub4="",
                sub5="",
                sub6="",
                academicyear=title,
                mail=arrmail[k],
            )
            new_entry.save()
            k = k + 1
        return HttpResponse("OK", status=status.HTTP_200_OK)


class phasestatusview(generics.ListCreateAPIView):
    queryset = phaseno.objects.all()
    serializer_class = Phasenoserializer


class subselect(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class = Addclassserializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        tid = requestbody["tid"]
        count = requestbody["no"]
        sub1 = requestbody["sub1"]
        sub2 = requestbody["sub2"]
        sub3 = requestbody["sub3"]
        sub4 = requestbody["sub4"]
        sub5 = requestbody["sub5"]
        sub6 = requestbody["sub6"]

        teacherid = Teacher.objects.get(tid=tid)
        current_year = date.today().year
        exp = current_year - int(teacherid.year.strftime("%Y"))
        subarray=[]
        p = Phase.objects.all()

        for i in p:
            
            if   i.sub1!='':
                d={}
                d['sub1']=i.sub1
                subarray.append(d)

            if i.sub2!='':
                d={}
                d['sub2']=i.sub2
                subarray.append(d)
                print(i.pid)
            
            if i.sub3!='':
                d={}
                d['sub3']=i.sub3
                subarray.append(d)

            if i.sub4!='':
                d={}
                d['sub4']=i.sub4
                subarray.append(d)
            
            if i.sub5!='':
                d={}
                d['sub5']=i.sub5
                subarray.append(d)

            if i.sub6!='':
                d={}
                d['sub6']=i.sub6
                subarray.append(d)
        
        print(subarray)

        def fun_order(sub,i):
        
                        if(i=='sub1'):
                            p = Phase.objects.get(sub1=sub)
                        elif(i=='sub2'):
                            p = Phase.objects.get(sub2=sub)
                        elif(i=='sub3'):
                            p = Phase.objects.get(sub3=sub)
                        elif(i=='sub4'):
                            p = Phase.objects.get(sub4=sub)
                        elif(i=='sub5'):
                            p = Phase.objects.get(sub5=sub)
                        elif(i=='sub6'):
                            p = Phase.objects.get(sub6=sub)

                        if p.exp < exp :
                            if(i=='sub1'):
                                p.sub1=''
                            elif(i=='sub2'):
                                p.sub2=''
                            elif(i=='sub3'):
                                p.sub3=''
                            elif(i=='sub4'):
                                p.sub4=''
                            elif(i=='sub5'):
                                p.sub5=''
                            elif(i=='sub6'):
                                p.sub6=''
                            print(p.mail)
                            p.status='UPDATE'
                            p.no=p.no-1
                            classid = ClassDivisions.objects.get(classid=sub)
                            classid.exp = exp
                            classid.save()
                            p.save()

        for k in subarray:
            for i,j in k.items():
                if sub1==j :
                        fun_order(sub1,i)
                            
                if sub2==j :
                        fun_order(sub2,i)
                
                if sub3==j :
                        fun_order(sub3,i)
                
                if sub4==j :
                        fun_order(sub4,i)
                
                if sub5==j :
                        fun_order(sub5,i)
                
                if sub6==j :
                        fun_order(sub6,i)
                
                
        i = 1
        while i <= count:
            sub = requestbody["sub" + str(i)]
            if sub!='':
                classid = ClassDivisions.objects.get(classid=sub)
                classid.exp = exp
                classid.classalloc = 1
                classid.save()
            i = i + 1

        phaseid = Phase.objects.get(tid=tid)
        phaseid.no = count
        phaseid.sub1 = sub1
        phaseid.sub2 = sub2
        phaseid.sub3 = sub3
        phaseid.sub4 = sub4
        phaseid.sub5 = sub5
        phaseid.sub6 = sub6
        phasenoid = phaseno.objects.all()
        val = phasenoid[0].no
        phaseid.academicyear = val

        phaseid.mail = teacherid.tmail
        phaseid.status = "OFF"
        phaseid.save()

        return HttpResponse("OK", status=status.HTTP_200_OK)


class Finalview(generics.CreateAPIView):
    serializer_class =Finalserializer

    def post(self, request, *args, **kwargs):
        requestbody = dict(request.data)
        p=Phase.objects.all()
        clash.objects.all().delete()
        arrtid=[]
        for i in p:
            nosub=i.no
            
            t=i.tid
            teacherobj=Teacher.objects.get(tid=t.tid)
            pos=teacherobj.pos

            flag=0
            if pos==2 or pos==1:
                if nosub<1:
                    flag=1
            elif pos==0:
                if nosub<2:
                    flag=1

            
            if(flag==1):
                arrtid.append(t.tid)
                new_entry =clash(clasid=t.tid)
                new_entry.save()

        print(arrtid)

        if len(arrtid)!=0:
            return HttpResponse(arrtid, status=status.HTTP_200_OK)

        elif len(arrtid)==0:
            p1=Phase.objects.all()
            clash.objects.all().delete()
            for i in p1:
                nosub=i.no
                t=i.tid
                sub1=i.sub1
                sub2=i.sub2
                sub3=i.sub3
                sub4=i.sub4
                sub5=i.sub5
                sub6=i.sub6
                pno=phaseno.objects.all()
                year=pno[0].no

                no = random.randint(10000, 99999)
                no = "S" + str(no)
                

                new_val=TeacherSelection(tid=t,
                sub1=sub1,
                sub2=sub2,
                sub3=sub3,
                sub4=sub4,
                sub5=sub5,
                sub6=sub6,
                count=nosub,
                selectionid=no,
                year=year)

                new_val.save()
                new_entry =clash(clasid='OK')
                new_entry.save()
            return HttpResponse("ok", status=status.HTTP_200_OK)
                


class TeacherSelectionview(generics.ListCreateAPIView):
    queryset = TeacherSelection.objects.all()
    serializer_class = TeacherSelectionserializer



class clashview(generics.ListCreateAPIView):
    queryset = clash.objects.all()
    serializer_class = clashserializer




