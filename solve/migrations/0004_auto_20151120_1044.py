# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solve', '0003_auto_20151120_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudokusolverlog',
            name='input_sudoku',
            field=models.TextField(default='null'),
        ),
    ]
