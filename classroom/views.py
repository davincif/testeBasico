from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator

from .models import Classroom


def classrooms(request):
    print("classrooms")
    if request.method == 'GET':
        # getting objects
        classrooms_list = Classroom.objects.all()
        paginator = Paginator(classrooms_list, 5)

        # getting requested page
        page_number = request.GET.get('page')
        page_number = page_number if page_number is not None else 1
        print("page_number", page_number)
        page_obj = paginator.get_page(page_number)
        print("paginator", page_obj)

        return render(request, 'classrooms.html', {'classrooms': page_obj})
    else:
        return HttpResponseForbidden()
