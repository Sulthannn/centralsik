# Generated by Django 4.1.2 on 2023-01-04 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belajar_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='durasi',
        ),
    ]