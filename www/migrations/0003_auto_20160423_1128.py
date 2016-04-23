# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 11:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20160423_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(db_index=True, default=datetime.datetime(2016, 4, 23, 11, 28, 58, 925343, tzinfo=utc), editable=False, verbose_name='Add date')),
                ('update_date', models.DateTimeField(default=datetime.datetime(2016, 4, 23, 11, 28, 58, 925409, tzinfo=utc), editable=False, verbose_name='Update date')),
                ('points', jsonfield.fields.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='token',
            name='add_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 4, 23, 11, 28, 58, 925343, tzinfo=utc), editable=False, verbose_name='Add date'),
        ),
        migrations.AlterField(
            model_name='token',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 23, 11, 28, 58, 925409, tzinfo=utc), editable=False, verbose_name='Update date'),
        ),
    ]
