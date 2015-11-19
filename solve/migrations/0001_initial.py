# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SudokuSolverLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('input_sudoku', models.CharField(max_length=100, default='null')),
                ('result', models.IntegerField(max_length=1, default=0)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
