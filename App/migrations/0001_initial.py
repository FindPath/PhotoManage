# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recordId', models.UUIDField(blank=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('rootId', models.CharField(max_length=20)),
                ('addtime', models.DateTimeField(blank=True)),
                ('updateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recordId', models.UUIDField(blank=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('rootId', models.CharField(max_length=20)),
                ('addtime', models.DateTimeField(blank=True)),
                ('updateTime', models.DateTimeField()),
                ('photoUrl', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.TextField()),
            ],
        ),
    ]
