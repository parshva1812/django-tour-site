# Generated by Django 3.2 on 2021-05-17 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210507_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From_date', models.DateField()),
                ('To_date', models.DateField()),
                ('Persons', models.IntegerField()),
                ('Amount', models.FloatField()),
                ('Payment_Method', models.CharField(max_length=100)),
                ('Payment_status', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tour')),
            ],
        ),
    ]