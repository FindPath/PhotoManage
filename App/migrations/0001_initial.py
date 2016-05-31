# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('rootId', models.CharField(max_length=20)),
                ('addtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('rootId', models.CharField(max_length=20)),
                ('addtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('photoUrl', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.TextField()),
                ('Album', models.ForeignKey(to='App.Album')),
            ],
        ),
    ]
