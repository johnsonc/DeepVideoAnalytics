# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0003_video_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='detection',
            name='metadata',
            field=models.TextField(default=''),
        ),
    ]
