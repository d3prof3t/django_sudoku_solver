# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solve', '0002_auto_20151119_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudokusolverlog',
            name='input_sudoku',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
