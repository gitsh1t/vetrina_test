# Generated by Django 2.2.16 on 2021-03-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0012_nuovo_utente'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_gallery',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='slider_1',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
