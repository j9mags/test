# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perishabletoken',
            name='expires_at',
            field=models.DateTimeField(editable=False),
        ),
    ]
