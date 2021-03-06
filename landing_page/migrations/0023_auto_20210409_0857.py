# Generated by Django 3.1.7 on 2021-04-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0022_auto_20210408_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider_1',
            name='content_prima_slide',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider_1',
            name='content_seconda_slide',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider_1',
            name='content_terza_slide',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider_1',
            name='titolo_prima_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='slider_1',
            name='titolo_seconda_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='slider_1',
            name='titolo_terza_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='content_prima_slide',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='content_seconda_slide',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='content_terza_slide',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='titolo_prima_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='titolo_seconda_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='slider_2',
            name='titolo_terza_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='slider_1',
            name='descrizione_prima_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='slider_1',
            name='descrizione_seconda_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='slider_1',
            name='descrizione_terza_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='slider_2',
            name='descrizione_prima_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='slider_2',
            name='descrizione_seconda_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='slider_2',
            name='descrizione_terza_slide',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
