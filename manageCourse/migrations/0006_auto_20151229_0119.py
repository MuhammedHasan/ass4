# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 01:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageCourse', '0005_auto_20151227_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='studens',
            new_name='students',
        ),
    ]