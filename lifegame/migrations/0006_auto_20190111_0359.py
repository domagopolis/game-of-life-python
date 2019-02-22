# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-11 03:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifegame', '0005_world_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=1)),
                ('health', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(default=True)),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_father', to='lifegame.LifeForm')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_mother', to='lifegame.LifeForm')),
            ],
        ),
        migrations.AddField(
            model_name='world',
            name='food_distribution',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='world',
            name='life_distribution',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='lifeform',
            name='world',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifegame.World'),
        ),
    ]