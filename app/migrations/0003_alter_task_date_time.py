# Generated by Django 5.0.3 on 2024-03-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_task_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
