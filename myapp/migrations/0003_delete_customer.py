# Generated by Django 3.2 on 2021-05-03 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer_added_on'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]