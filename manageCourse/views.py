from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from forms import *
from models import *


@csrf_protect
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            Student(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            ).save()
            return redirect('/list-student/')
        return render(request, 'createStudent.html', {'form': form})
    return render(request, 'createStudent.html', {'form': StudentForm()})


@csrf_protect
def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                office_details=form.cleaned_data['office_details']
            ).save()
            return redirect('/list-teacher/')
        return render(request, 'createTeacher.html', {'form': form})
    return render(request, 'createTeacher.html', {'form': TeacherForm()})


@csrf_protect
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            Course(
                name=form.cleaned_data['name'],
                code=form.cleaned_data['code'],
                classroom=form.cleaned_data['classroom'],
                times=form.cleaned_data['times'],
            ).save()
            return redirect('/list-course/')
        return render(request, 'createCourse.html', {'form': form})
    return render(request, 'createCourse.html', {'form': CourseForm()})


def course_register(request):
    if request.method == "POST":
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            course = Course.objects.get(pk=form.cleaned_data['course'])
            course.students = Student.objects.filter(
                id__in=form.cleaned_data['students'])
            course.save()
        return redirect('/list-registered-course/')
    return render(request, 'courseRegister.html', {
        'forms': [
            (i.name, CourseRegisterForm({'course': i.pk}))
            for i in Course.objects.all()
        ],
    })


def list_course_register(request):
    return render(request, 'listOfRegisteredCourse.html', {
        'courses': Course.objects.all()
    })


def list_student(request):
    return render(
        request, 'listOfStudent.html',
        {
            'students': Student.objects.all()
        }
    )


def list_teacher(request):
    return render(
        request, 'listOfTeacher.html',
        {
            'teachers': Teacher.objects.all()
        }
    )


def list_course(request):
    return render(
        request, 'listOfCourse.html',
        {
            'courses': Course.objects.all()
        }
    )
