# Generated by Django 4.1.6 on 2023-02-12 14:20
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
