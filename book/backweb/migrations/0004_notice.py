# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0003_art_is_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('icon', models.ImageField(null=True, upload_to='article')),
                ('is_display', models.BooleanField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'notice',
            },
        ),
    ]