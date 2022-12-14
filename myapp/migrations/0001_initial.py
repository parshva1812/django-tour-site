# Generated by Django 3.2 on 2021-05-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Mname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('Genders', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Phone', models.CharField(max_length=10, unique=True)),
                ('Address', models.TextField(max_length=500)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
