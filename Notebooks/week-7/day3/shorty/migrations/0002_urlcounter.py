# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlCounter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('record', models.ForeignKey(to='shorty.UrlRecord')),
            ],
        ),
    ]
