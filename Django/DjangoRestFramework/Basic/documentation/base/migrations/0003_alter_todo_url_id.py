# Generated by Django 5.0.6 on 2024-05-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_todo_created_at_alter_todo_url_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='url_id',
            field=models.UUIDField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]
