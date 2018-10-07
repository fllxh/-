from django.db import models


# Create your models here.

class StudentInfo(models.Model):
    Stu_name = models.CharField(max_length=32)
