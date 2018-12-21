# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-21 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NasaComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField()),
                ('rating', models.IntegerField()),
                ('imageURL', models.URLField()),
            ],
        ),
    ]
