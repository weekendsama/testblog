# Generated by Django 3.0.7 on 2020-06-27 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 14, 46, 8, 876738, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
