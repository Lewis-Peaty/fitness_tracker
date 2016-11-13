# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-13 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=2, max_digits=3),
        ),
    ]