from rest_framework import serializers
from .models import Teacher,Subject,AdminLogin,TeacherLogin,ClassDivisions,otherSubject
from .models import Department,phaseno,Phase,TeacherSelection,Final,clash,semtype,phaseget,Phaseteacher
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

class Finalserializer(serializers.ModelSerializer):
    class Meta:
        model=Final
        fields=['val'] 
class TeacherSelectionserializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherSelection
        fields=['tid','sub1','sub2','count','selectionid','year'] 

class  ClassDivisionsserializer(serializers.ModelSerializer):
     class Meta:
        model=ClassDivisions
        fields=['classid','classname','subject','depid','classalloc','exp','sem','subtype'] 


class Phaseserializer(serializers.ModelSerializer):
    class Meta:
        model=Phase
        fields=['no','tid','alloc','status','sub1','sub2','sub3','sub4','sub5','sub6','academicyear','mail']



class Phasenoserializer(serializers.ModelSerializer):
    class Meta:
        model=phaseno
        fields=['no','active']

class clashserializer(serializers.ModelSerializer):
    class Meta:
        model=clash
        fields=['clashid']



class Addclassserializer(serializers.ModelSerializer):
    class Meta:
        model=Phase
        fields=['no','tid','sub1','sub2','sub3','sub4','sub5','sub6']

class otherSubjectserializer(serializers.ModelSerializer):
    class Meta:
        model=otherSubject
        fields=['subid','subname','sem','depid','subtype','count']

class Semtypeserializer(serializers.ModelSerializer):
    class Meta:
        model=semtype
        fields=['sem']

class phasegetserializer(serializers.ModelSerializer):

    class Meta:
        model=phaseget
        fields=['val']

class phaseteacherserializer(serializers.ModelSerializer):

    class Meta:
        model=Phaseteacher
        fields=['tname','sub1','classname1','sub2','classname2','sub3','classname3',
        'sub4','classname4','sub5','classname5','sub6','classname6']