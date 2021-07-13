from django.shortcuts import render
from django.http import HttpResponseForbidden


def teachers(request):
    if request.method == 'GET':
        return render(request, 'teachers.html')
    else:
        return HttpResponseForbidden()
