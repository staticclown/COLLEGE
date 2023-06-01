from rest_framework import serializers
from .models import Teacher,Subject

class Teacherserializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['tname','tmail','gender','tid','password','year','depid']


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subid','subname','sem','depid']
        