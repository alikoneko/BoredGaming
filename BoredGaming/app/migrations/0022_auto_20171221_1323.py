# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]