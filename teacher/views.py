from django.shortcuts import redirect, render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from django.core.paginator import Paginator

from .models import Teacher
from .forms import TeacherForm
from classroom.models import Classroom


def teachers(request):
    if request.method == 'GET':
        # getting objects
        teachers_list = Teacher.objects.select_related().all().order_by('id')
        paginator = Paginator(teachers_list, 5)

        # getting requested page
        page_number = request.GET.get('page')
        page_number = page_number if page_number is not None else 1
        page_obj = paginator.get_page(page_number)

        return render(request, 'teachers.html', {'teachers': page_obj})
    else:
        return HttpResponseForbidden()


def teacher_details(request):
    if request.method == 'POST':
        info = __get_details(request)[0]
        form = TeacherForm(request.POST, instance=info)
        classrooms = Classroom.objects.all().order_by('name')

        if form.is_valid():
            try:
                info.save()
            except Exception:
                return HttpResponseServerError("Impossible to edit teacher")

        return render(
            request,
            'teacher_details.html',
            {'info': info, 'form': form, 'classrooms': classrooms}
        )
    elif request.method == 'GET':
        info = __get_details(request)[0]
        form = TeacherForm(instance=info)
        classrooms = Classroom.objects.all().order_by('name')

        return render(
            request,
            'teacher_details.html',
            {'info': info, 'form': form, 'classrooms': classrooms}
        )
    else:
        return HttpResponseForbidden()


def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            try:
                info = Teacher(
                    name=form.cleaned_data.get('name'),
                    classroom=form.cleaned_data.get('classroom')
                )
                info.save()
            except Exception:
                return HttpResponseServerError("Impossible to save teacher")

            return redirect('teachers_url')
        else:
            classrooms = Classroom.objects.all().order_by('name')

            return render(request, 'teacher_add.html', {'form': form, 'classrooms': classrooms})
    if request.method == 'GET':
        classrooms = Classroom.objects.all().order_by('name')
        form = TeacherForm()

        return render(request, 'teacher_add.html', {'form': form, 'classrooms': classrooms})
    else:
        return HttpResponseForbidden()


def teacher_delete(request):
    if request.method == 'POST':
        info = __get_details(request)[0]

        try:
            info.delete()
        except Exception:
            return HttpResponseServerError("Impossible to delete teacher")

        return redirect('teachers_url')
    else:
        return HttpResponseForbidden()


def __get_details(request):
    teacher_id = request.GET.get('cr')

    try:
        teacher_id = int(teacher_id)
    except Exception:
        return HttpResponseBadRequest("id's not a int")

    if teacher_id <= 0:
        return HttpResponseBadRequest("id's not present")

    info = Teacher.objects.filter(id=teacher_id)

    if len(info) <= 0:
        return HttpResponseBadRequest('no teacher found with this id')

    return info
