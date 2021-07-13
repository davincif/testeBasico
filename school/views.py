from django.shortcuts import render
from django.http import HttpResponseForbidden


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        return HttpResponseForbidden()
