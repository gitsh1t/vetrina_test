# Generated by Django 3.1.7 on 2021-04-21 12:03

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0028_auto_20210421_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='img_hero',
            name='colore_titolo',
            field=colorful.fields.RGBColorField(default='black'),
        ),
    ]
