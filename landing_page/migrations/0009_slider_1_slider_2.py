# Generated by Django 2.2.16 on 2021-03-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0008_auto_20210121_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_prima_slide', models.ImageField(blank=True, upload_to='img-slider-1/1')),
                ('image_seconda_slide', models.ImageField(blank=True, upload_to='img-slider-1/2')),
                ('image_terza_slide', models.ImageField(blank=True, upload_to='img-slider-1/3')),
                ('descrizione_prima_slide', models.TextField()),
                ('descrizione_seconda_slide', models.TextField()),
                ('descrizione_terza_slide', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='slider_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_prima_slide', models.ImageField(blank=True, upload_to='img-slider-1/1')),
                ('image_seconda_slide', models.ImageField(blank=True, upload_to='img-slider-1/2')),
                ('image_terza_slide', models.ImageField(blank=True, upload_to='img-slider-1/3')),
                ('descrizione_prima_slide', models.TextField()),
                ('descrizione_seconda_slide', models.TextField()),
                ('descrizione_terza_slide', models.TextField()),
            ],
        ),
    ]
