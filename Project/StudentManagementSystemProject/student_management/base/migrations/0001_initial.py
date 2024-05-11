# Generated by Django 5.0.5 on 2024-05-10 08:31

import base.models
import django.db.models.deletion
import django_enumfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('teacher', models.BooleanField(default=True)),
                ('student', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('faculty', models.ManyToManyField(to='base.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('birth_date', models.DateField(default=None)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('id_type', django_enumfield.db.fields.EnumField(default=2, enum=base.models.TypeEnum)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='base.faculty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('birth_date', models.DateField(default=None)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('id_type', django_enumfield.db.fields.EnumField(default=1, enum=base.models.TypeEnum)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='base.faculty')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
