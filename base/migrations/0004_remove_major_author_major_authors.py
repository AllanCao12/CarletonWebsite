# Generated by Django 4.2.13 on 2024-07-22 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_extra_major_author_remove_major_resources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='author',
        ),
        migrations.AddField(
            model_name='major',
            name='authors',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
