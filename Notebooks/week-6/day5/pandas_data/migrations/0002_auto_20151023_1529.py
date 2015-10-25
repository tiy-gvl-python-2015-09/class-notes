# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from play import load_data


class Migration(migrations.Migration):

    dependencies = [
        ('pandas_data', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
