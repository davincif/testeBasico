from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.core.paginator import Paginator

from .models import Classroom
from .forms import ClassroomForm


def classrooms(request):
    if request.method == 'GET':
        # getting objects
        classrooms_list = Classroom.objects.all().order_by('id')
        paginator = Paginator(classrooms_list, 5)

        # getting requested page
        page_number = request.GET.get('page')
        page_number = page_number if page_number is not None else 1
        page_obj = paginator.get_page(page_number)

        return render(request, 'classrooms.html', {'classrooms': page_obj})
    else:
        return HttpResponseForbidden()


def classroom_details(request):
    if request.method == 'POST':
        info = __get_details(request)[0]
        form = ClassroomForm(request.POST, instance=info)

        if form.is_valid():
            info.name = form.cleaned_data.get('name')
            try:
                info.save()
            except Exception:
                return HttpResponseServerError("Impossible to edit classrom")

        return render(request, 'classroom_details.html', {'info': info, 'form': form})
    elif request.method == 'GET':
        info = __get_details(request)[0]
        form = ClassroomForm(instance=info)

        return render(request, 'classroom_details.html', {'info': info, 'form': form})
    else:
        return HttpResponseForbidden()


def classroom_add(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            try:
                info = Classroom(name=form.cleaned_data.get('name'))
                info.save()
            except Exception:
                return HttpResponseServerError("Impossible to save classrom")

        return redirect('classrooms_url')
    if request.method == 'GET':
        form = ClassroomForm()

        return render(request, 'classroom_add.html', {'form': form})
    else:
        return HttpResponseForbidden()


def classroom_delete(request):
    if request.method == 'POST':
        info = __get_details(request)[0]

        try:
            info.delete()
        except Exception:
            return HttpResponseServerError("Impossible to delete classrom")

        return redirect('classrooms_url')
    else:
        return HttpResponseForbidden()


def __get_details(request):
    classroom_id = request.GET.get('cr')

    try:
        classroom_id = int(classroom_id)
    except Exception:
        return HttpResponseBadRequest("id's not a int")

    if classroom_id <= 0:
        return HttpResponseBadRequest("id's not present")

    info = Classroom.objects.filter(id=classroom_id)

    if len(info) <= 0:
        return HttpResponseBadRequest('no classroom found with this id')

    return info
