from rest_framework import serializers
from .models import Teacher,Subject,AdminLogin,TeacherLogin
from .models import TeacherSelection,ClassDivisions
class Teacherserializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['tname','tmail','gender','tid','password','year','depid']


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subid','subname','sem','depid']
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
        fields=['tid','sub1','sub2','sub3','sub4','count'] 


class  ClassDivisionsserializer(serializers.ModelSerializer):
     class Meta:
        model=ClassDivisions
        fields=['classname','subject','depid','alloc','exp'] 

