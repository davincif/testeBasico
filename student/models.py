from django.db import models

from teacher.models import Teacher


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.name)
