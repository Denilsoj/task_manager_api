# Generated by Django 5.1.1 on 2024-09-12 14:40

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_time_task_time_start'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='task',
            name='unique_title_per_user',
        ),
        migrations.AlterField(
            model_name='task',
            name='time_end',
            field=models.TimeField(blank=True, default=datetime.time(23, 59), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_start',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('title', 'user', 'date'), name='unique_title_per_user'),
        ),
    ]
