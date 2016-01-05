from django import forms
from models import *


class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    office_details = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=18)
    email = forms.EmailField(max_length=30)


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()


class CourseForm(forms.Form):
    name = forms.CharField(max_length=30)
    code = forms.CharField(max_length=30)
    classroom = forms.CharField(max_length=10)
    times = forms.CharField(max_length=30)


class CourseRegisterForm(forms.Form):
    course = forms.CharField(widget=forms.HiddenInput())
    students = forms.ModelMultipleChoiceField(queryset=Student.objects)
