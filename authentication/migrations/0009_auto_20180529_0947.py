# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-29 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20171113_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvupload',
            name='course',
        ),
        migrations.AddField(
            model_name='csvupload',
            name='upload_type',
            field=models.CharField(default='st', max_length=2),
            preserve_default=False,
        ),
    ]