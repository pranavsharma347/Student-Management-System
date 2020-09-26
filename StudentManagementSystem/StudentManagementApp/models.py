from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    Rollno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=264)
    LastName=models.CharField(max_length=264)
    Course = models.CharField(max_length=264)
    Mobileno=models.CharField(max_length=10)
    Email=models.EmailField()
    Address=models.CharField(max_length=264)
    objects=models.Manager