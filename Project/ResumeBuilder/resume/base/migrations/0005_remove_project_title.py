# Generated by Django 5.0.6 on 2024-05-16 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
    ]
