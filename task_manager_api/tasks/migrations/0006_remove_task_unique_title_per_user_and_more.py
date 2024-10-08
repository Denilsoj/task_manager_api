# Generated by Django 5.1.1 on 2024-09-14 20:51

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_unique_title_per_user_and_more'),
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
            field=models.TimeField(blank=True, default=datetime.time(23, 59, 59), null=True),
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('title', 'user', 'date'), name='unique_title_per_user_date'),
        ),
    ]
