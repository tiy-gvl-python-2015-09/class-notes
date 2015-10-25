# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('student_name', models.CharField(max_length=100)),
                ('mb', models.CharField(max_length=4)),
                ('year', models.IntegerField()),
                ('house', models.CharField(max_length=20)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
