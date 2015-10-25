from django.db import models

# Create your models here.
#    Student Name    MB  Year       House       GPA


class StudentRecord(models.Model):
    student_name = models.CharField(max_length=100)
    mb = models.CharField(max_length=4)
    year = models.IntegerField()
    house = models.CharField(max_length=20)
    gpa = models.FloatField()