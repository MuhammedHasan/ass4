from __future__ import unicode_literals

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office_details = models.CharField(max_length=30)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=30)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Course(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    classroom = models.CharField(max_length=10)
    times = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, null=True)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.name
