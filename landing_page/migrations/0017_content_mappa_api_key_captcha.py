# Generated by Django 2.2.16 on 2021-03-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0016_auto_20210326_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='content_mappa',
            name='api_key_captcha',
            field=models.CharField(default='nokey', max_length=250),
        ),
    ]
