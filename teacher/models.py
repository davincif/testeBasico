from django.db import models

from classroom.models import Classroom


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=False)
