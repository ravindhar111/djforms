from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100,primary_key=True)
    sclocation=models.CharField(max_length=100)
    scprincipal=models.CharField(max_length=20)

class Student(models.Model):
    scname=models.ForeignKey(School,on_delete=models.CASCADE)
    stname=models.CharField(max_length=40)
    stage=models.IntegerField()
    