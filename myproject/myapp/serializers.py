from rest_framework import serializers
from .models import Teacher,Subject,AdminLogin,TeacherLogin
from .models import TeacherSelection,ClassDivisions,Department,Phase,phaseno
class Teacherserializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['tname','tmail','gender','tid','password','year','depid','pos']

class Departmentserializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields=['depid','depname','HODname','division']
        

class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subid','subname','sem','depid','subtype']
class AdminLoginserializer(serializers.ModelSerializer):
    class Meta:
        model=AdminLogin
        fields=['aid','password']     

class TeacherLoginserializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherLogin
        fields=['Tid','password'] 

class TeacherSelectionserializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherSelection
        fields=['tid','sub1','sub2','sub3','sub4','count','selectionid'] 


class  ClassDivisionsserializer(serializers.ModelSerializer):
     class Meta:
        model=ClassDivisions
        fields=['classname','subject','depid','classalloc','exp','sem'] 


class Phaseserializer(serializers.ModelSerializer):
    class Meta:
        model=Phase
        fields=['no','tid','alloc','status','sub1','sub2','lab1','lab2','academicyear','mail']

class Phasenoserializer(serializers.ModelSerializer):
    class Meta:
        model=phaseno
        fields=['no','active']


