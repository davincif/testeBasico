from django.shortcuts import render
from django.http import HttpResponseForbidden


def students(request):
    if request.method == 'GET':
        return render(request, 'students.html')
    else:
        return HttpResponseForbidden()
