# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-03 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifegame', '0003_world_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='feature',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
