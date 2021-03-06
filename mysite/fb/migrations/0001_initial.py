# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('main_question_id', models.IntegerField()),
                ('answer', models.TextField(null=True)),
                ('score_range', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('apply_num', models.IntegerField(null=True)),
                ('classification', models.TextField(null=True)),
                ('subtitle', models.TextField(null=True)),
                ('main_quest', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('sub_question_id', models.IntegerField()),
                ('option', models.TextField(null=True)),
                ('score', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('main_question_id', models.IntegerField()),
                ('main_quest', models.TextField(null=True)),
            ],
        ),
    ]
