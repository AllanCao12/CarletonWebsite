# Generated by Django 4.2.13 on 2024-07-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_events_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='clubNume',
            field=models.CharField(max_length=100),
        ),
    ]
