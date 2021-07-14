from django.urls import path

from . import views

urlpatterns = [
    path('', views.classrooms, name='classrooms_url'),
    path('details/', views.classroom_details, name='classroom_details_url'),
]
