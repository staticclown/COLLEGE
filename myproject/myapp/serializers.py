from rest_framework import serializers
from .models import Teacher,Subject,Login

class Teacherserializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['tname','tmail','gender','tid','password','year','depid']


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subid','subname','sem','depid']
class Loginserializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['pid','passsword']     
