# Generated by Django 3.2.19 on 2023-08-24 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230824_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
