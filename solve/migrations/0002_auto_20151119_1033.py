# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudokusolverlog',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
