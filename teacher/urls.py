from django.urls import path

from . import views

urlpatterns = [
    path('', views.teachers, name='teachers_url'),
    path('details/', views.teacher_details, name='teacher_details_url'),
    path('details/delete/', views.teacher_delete, name='teacher_details_url'),
    path('add/', views.teacher_add, name='teacher_add_url'),
]
