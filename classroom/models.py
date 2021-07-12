from django.db import models


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.name)
