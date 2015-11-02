# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20151026_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 26, 15, 13, 58, 763189), auto_now_add=True),
            preserve_default=False,
        ),
    ]
