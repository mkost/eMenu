# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations

fixture = 'dishes'


def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='emenu')


def reverse_fixture(apps, schema_editor):
    return True


class Migration(migrations.Migration):

    dependencies = [
        ('emenu', '0004_auto_20161206_2234'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_fixture),
    ]
