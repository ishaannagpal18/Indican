# Generated by Django 3.2.7 on 2022-01-06 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dob_dayofyear_internal',
        ),
    ]