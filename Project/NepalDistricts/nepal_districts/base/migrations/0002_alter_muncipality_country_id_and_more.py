# Generated by Django 5.0.6 on 2024-06-12 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muncipality',
            name='country_id',
            field=models.ForeignKey(default=156, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muncipality', to='base.country'),
        ),
        migrations.AlterField(
            model_name='province',
            name='country_id',
            field=models.ForeignKey(default=156, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='province', to='base.country'),
        ),
    ]
