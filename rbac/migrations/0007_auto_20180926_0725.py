# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-26 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0006_permission_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='URL别名'),
        ),
    ]