from django.db import models

from teacher.models import Teacher


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=False)
