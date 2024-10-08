# Generated by Django 5.1.1 on 2024-09-09 12:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name='tasks',
            constraint=models.UniqueConstraint(fields=('title', 'user'), name='unique_title_per_user'),
        ),
    ]
