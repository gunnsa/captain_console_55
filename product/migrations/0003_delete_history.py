# Generated by Django 3.0.5 on 2020-05-08 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_history'),
    ]

    operations = [
        migrations.DeleteModel(
            name='History',
        ),
    ]
