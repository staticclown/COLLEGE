from django.db import models
# Create your models here.
class Department(models.Model):
    depid=models.CharField(max_length=15,primary_key=True)
    depname=models.CharField(max_length=10,default=None)
    HODname=models.CharField(max_length=25,default=None)
    division=models.IntegerField(default=0)

class Subject(models.Model):
    subid=models.CharField(max_length=25,primary_key=True)
    subname=models.CharField(max_length=25)
    sem=models.CharField(max_length=10)
    year=models.CharField(max_length=10,default='2022')
    depid=models.ForeignKey(Department, on_delete=models.CASCADE,default='D0001') 
    subtype=models.CharField(max_length=5,default='T')
    
   


class Teacher(models.Model):
    tname=models.CharField(max_length=15)
    tmail=models.CharField(max_length=35,default=None)
    gender=models.CharField(max_length=10)
    tid=models.CharField(max_length=10,primary_key=True)
    #qualifications=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    year=models.DateField()
    depid=models.ForeignKey(Department, on_delete=models.CASCADE,default='D0001') 
    pos=models.IntegerField(default=0)

class AdminLogin(models.Model):
    aid=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=10)

class TeacherLogin(models.Model):
    Tid=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class TeacherSelection(models.Model):
    tid=models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    sub1=models.CharField(max_length=10) 
    sub2=models.CharField(max_length=10)
    sub3=models.CharField(max_length=10)
    sub4=models.CharField(max_length=10)
    count=models.IntegerField()
    selectionid=models.CharField(max_length=20,primary_key=True)


class ClassDivisions(models.Model):
    classname=models.CharField(max_length=20,primary_key=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    classalloc=models.CharField(max_length=10)
    exp=models.IntegerField()
    sem=models.CharField(max_length=20)

class Phase(models.Model):
    no=models.IntegerField()
    tid=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    alloc=models.IntegerField(default=0)
    status=models.CharField(max_length=20,default='ON')
    exp=models.IntegerField()
    sub1=models.CharField(max_length=20,default=None)
    sub2=models.CharField(max_length=20,default=None)
    lab1=models.CharField(max_length=20,default=None)
    lab2=models.CharField(max_length=20,default=None)
    academicyear=models.CharField(max_length=20,default='2023')
    mail=models.CharField(max_length=20)

class phaseno(models.Model):
    no=models.CharField(max_length=20,primary_key=True)
    active=models.CharField(max_length=20)

