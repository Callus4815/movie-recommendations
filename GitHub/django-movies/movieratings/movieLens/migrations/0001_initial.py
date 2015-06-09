# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('gender', models.CharField(max_length=2)),
                ('age', models.IntegerField()),
                ('occupation', models.IntegerField()),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rating', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('movie', models.ForeignKey(to='movieLens.Movie')),
                ('rater', models.ForeignKey(to='movieLens.Rater')),
            ],
        ),
    ]
