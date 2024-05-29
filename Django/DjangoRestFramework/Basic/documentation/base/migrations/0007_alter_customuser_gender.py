# Generated by Django 5.0.6 on 2024-05-28 10:23

import base.enums
import django_enumfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=django_enumfield.db.fields.EnumField(blank=True, default=3, enum=base.enums.Gender_choice, null=True),
        ),
    ]
