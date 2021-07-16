from django.urls import path

from . import views

urlpatterns = [
    path('', views.students, name='students_url'),
    path('details/', views.student_details, name='student_details_url'),
    path('details/delete/', views.student_delete, name='student_details_url'),
    path('add/', views.student_add, name='student_add_url'),
]
