# Generated by Django 5.0.4 on 2024-05-03 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200, unique=True)),
                ('school_location', models.CharField(max_length=200)),
                ('school_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_location', models.CharField(max_length=200)),
                ('student_number', models.IntegerField(default=0)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.school')),
            ],
        ),
    ]
