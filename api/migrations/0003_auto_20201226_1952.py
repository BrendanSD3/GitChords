# Generated by Django 2.2.1 on 2020-12-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201226_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='chords',
            field=models.CharField(choices=[('A', 'A Chord'), ('G', 'G Chord'), ('D', 'D chord'), ('C', 'C chord'), ('F', 'F chord')], max_length=1),
        ),
    ]