# Generated by Django 2.2.1 on 2020-12-26 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]