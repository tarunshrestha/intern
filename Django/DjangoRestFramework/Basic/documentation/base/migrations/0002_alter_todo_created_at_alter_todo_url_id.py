# Generated by Django 5.0.6 on 2024-05-19 08:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='url_id',
            field=models.UUIDField(default=uuid.UUID('414028f3-dc7b-4981-9f1c-74bfc60a0108'), editable=False, primary_key=True, serialize=False),
        ),
    ]