# Generated by Django 2.2.16 on 2021-03-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0013_auto_20210326_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='titoli_landing_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scritta_centrale_pagina', models.TextField()),
                ('titolo_catalogo_prodotti', models.TextField()),
                ('current', models.BooleanField(default=False)),
            ],
        ),
    ]
