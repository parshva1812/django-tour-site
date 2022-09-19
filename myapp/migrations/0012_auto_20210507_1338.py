# Generated by Django 3.2 on 2021-05-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_night_days_tour_nights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='place_from',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tour',
            name='place_to',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_descriptions',
            field=models.TextField(max_length='5000'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_name',
            field=models.CharField(max_length=100),
        ),
    ]