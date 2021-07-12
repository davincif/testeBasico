from django.contrib import admin

from .models import Classroom


class ClassroomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


admin.site.register(Classroom, ClassroomAdmin)
