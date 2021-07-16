from django.urls import path

from . import views

urlpatterns = [
    path('', views.classrooms, name='classrooms_url'),
    path('details/', views.classroom_details, name='classroom_details_url'),
    path('details/delete/', views.classroom_delete, name='classroom_details_url'),
    path('add/', views.classroom_add, name='classroom_add_url'),
]
