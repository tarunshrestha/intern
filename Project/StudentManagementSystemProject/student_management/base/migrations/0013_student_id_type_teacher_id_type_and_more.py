# Generated by Django 5.0.5 on 2024-05-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_student_password_2_remove_teacher_password_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='id_type',
            field=models.CharField(default='Student', max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='id_type',
            field=models.CharField(default='Teacher', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
