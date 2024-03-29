from django.db import models

from classroom.models import Classroom


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.name)
