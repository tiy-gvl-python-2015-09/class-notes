# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0007_auto_20151022_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='color',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='make',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
