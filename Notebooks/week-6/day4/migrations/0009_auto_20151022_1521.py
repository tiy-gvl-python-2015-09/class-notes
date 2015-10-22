# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from helloworld.models import Person


def clean_people_with_asd_name(*args):
    Person.objects.filter(name="asd").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0008_auto_20151022_1511'),
    ]

    operations = [
        migrations.RunPython(clean_people_with_asd_name)
    ]
