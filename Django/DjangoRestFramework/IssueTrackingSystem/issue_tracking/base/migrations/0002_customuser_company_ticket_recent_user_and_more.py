# Generated by Django 5.0.6 on 2024-06-01 15:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.ManyToManyField(blank=True, default='', to='base.company'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='recent_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='token_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, default='', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, default='', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='company',
            field=models.ManyToManyField(blank=True, default='', to='base.company'),
        ),
    ]