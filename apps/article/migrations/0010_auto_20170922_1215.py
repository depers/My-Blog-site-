# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-22 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20170922_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='art',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='\u6587\u7ae0id'),
        ),
    ]
