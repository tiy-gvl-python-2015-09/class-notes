# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
