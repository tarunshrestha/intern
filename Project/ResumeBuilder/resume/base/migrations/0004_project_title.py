# Generated by Django 5.0.6 on 2024-05-16 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_enddate_job_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
