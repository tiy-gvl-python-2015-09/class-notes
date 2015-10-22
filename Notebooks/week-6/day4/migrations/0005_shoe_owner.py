# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0004_auto_20151021_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='owner',
            field=models.ForeignKey(default=0, to='helloworld.Person'),
            preserve_default=False,
        ),
    ]
