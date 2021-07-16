from django.shortcuts import redirect, render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from django.core.paginator import Paginator

from .models import Student
from .forms import StudentForm
from teacher.models import Teacher


def students(request):
    if request.method == 'GET':
        # getting objects
        student_list = Student.objects.select_related().all().order_by('id')
        paginator = Paginator(student_list, 5)

        # getting requested page
        page_number = request.GET.get('page')
        page_number = page_number if page_number is not None else 1
        page_obj = paginator.get_page(page_number)

        return render(request, 'students.html', {'students': page_obj})
    else:
        return HttpResponseForbidden()


def student_details(request):
    if request.method == 'POST':
        info = __get_details(request)[0]
        form = StudentForm(request.POST, instance=info)
        teachers = Teacher.objects.all().order_by('name')

        if form.is_valid():
            try:
                info.save()
            except Exception:
                return HttpResponseServerError("Impossible to edit student")

        return render(
            request,
            'student_details.html',
            {'info': info, 'form': form, 'teachers': teachers}
        )
    elif request.method == 'GET':
        print("\n", '+++', '\n')
        info = __get_details(request)[0]
        form = StudentForm(instance=info)
        teachers = Teacher.objects.all().order_by('name')
        print("\n", '****', '\n')

        return render(
            request,
            'student_details.html',
            {'info': info, 'form': form, 'teachers': teachers}
        )
    else:
        return HttpResponseForbidden()


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            try:
                info = Student(
                    name=form.cleaned_data.get('name'),
                    teacher=form.cleaned_data.get('teacher')
                )
                info.save()
            except Exception:
                return HttpResponseServerError("Impossible to save student")

            return redirect('students_url')
        else:
            teacher = Teacher.objects.all().order_by('name')

            return render(request, 'student_add.html', {'form': form, 'teachers': teacher})
    if request.method == 'GET':
        teacher = Teacher.objects.all().order_by('name')
        form = StudentForm()

        return render(request, 'student_add.html', {'form': form, 'teachers': teacher})
    else:
        return HttpResponseForbidden()


def student_delete(request):
    if request.method == 'POST':
        info = __get_details(request)[0]

        try:
            info.delete()
        except Exception:
            return HttpResponseServerError("Impossible to delete student")

        return redirect('students_url')
    else:
        return HttpResponseForbidden()


def __get_details(request):
    students_id = request.GET.get('cr')

    try:
        students_id = int(students_id)
    except Exception:
        return HttpResponseBadRequest("id's not a int")

    if students_id <= 0:
        return HttpResponseBadRequest("id's not present")

    info = Student.objects.filter(id=students_id)

    if len(info) <= 0:
        return HttpResponseBadRequest('no student found with this id')

    return info
