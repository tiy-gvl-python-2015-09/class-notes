# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0003_shoes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shoes',
            new_name='Shoe',
        ),
    ]
