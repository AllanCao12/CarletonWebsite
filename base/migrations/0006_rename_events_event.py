# Generated by Django 4.2.13 on 2024-07-30 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]