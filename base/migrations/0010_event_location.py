# Generated by Django 4.2.13 on 2024-07-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_event_clubname'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Carleton University', max_length=100),
        ),
    ]