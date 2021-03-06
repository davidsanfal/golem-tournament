# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 09:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Golem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('golem_type', models.CharField(max_length=60)),
                ('engine', models.IntegerField(default=0)),
                ('right_weapon', models.IntegerField(default=0)),
                ('left_weapon', models.IntegerField(default=0)),
                ('right_leg', models.IntegerField(default=0)),
                ('left_leg', models.IntegerField(default=0)),
                ('right_arm', models.IntegerField(default=0)),
                ('left_arm', models.IntegerField(default=0)),
                ('cabin', models.IntegerField(default=0)),
                ('helm', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='golems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=60)),
                ('level', models.IntegerField()),
                ('part_type', models.CharField(max_length=60)),
                ('golem_type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('part_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='golem_tournament.Part')),
                ('defense', models.IntegerField(default=0)),
            ],
            bases=('golem_tournament.part',),
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('part_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='golem_tournament.Part')),
            ],
            bases=('golem_tournament.part',),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('part_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='golem_tournament.Part')),
                ('weapon_range', models.IntegerField(default=0)),
                ('damage', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=1)),
                ('limit', models.IntegerField(default=0)),
            ],
            bases=('golem_tournament.part',),
        ),
    ]
