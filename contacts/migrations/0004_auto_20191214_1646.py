# Generated by Django 2.2.8 on 2019-12-14 11:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0003_auto_20191214_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 14, 16, 46, 39, 260921)),
        ),
    ]
