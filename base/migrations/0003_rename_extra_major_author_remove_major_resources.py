# Generated by Django 4.2.13 on 2024-07-22 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_course_major'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major',
            old_name='Extra',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='major',
            name='resources',
        ),
    ]
