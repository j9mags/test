# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 14:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_csv_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='csv_content',
        ),
        migrations.AddField(
            model_name='csvupload',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]