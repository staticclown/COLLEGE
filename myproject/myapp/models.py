from django.db import models
# Create your models here.
class Department(models.Model):
    depid=models.CharField(max_length=15,primary_key=True)
    depname=models.CharField(max_length=10,default=None)
    HODname=models.CharField(max_length=15,default=None)

class Subject(models.Model):
    subid=models.CharField(max_length=15,primary_key=True)
    subname=models.CharField(max_length=15)
    sem=models.CharField(max_length=10)
class Teacher(models.Model):
    tname=models.CharField(max_length=15)
    tmail=models.CharField(max_length=15,default=None)
    gender=models.CharField(max_length=10)
    tid=models.CharField(max_length=10,primary_key=True)
    qualifications=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    year=models.DateField()
    depid=models.ForeignKey(Department, on_delete=models.CASCADE,default='D0001') 
