from django.db import models

# Create your models here.
class Teacher(models.Model):
    t_name=models.CharField(max_length=15)
    gender=models.CharField(max_length=2)
    t_id=models.CharField(max_length=10,primary_key=True)
    qualifications=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    year=models.DateField()
    