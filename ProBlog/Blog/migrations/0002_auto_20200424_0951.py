# Generated by Django 3.0.3 on 2020-04-24 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 24, 7, 51, 16, 202411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 7, 51, 16, 201412, tzinfo=utc)),
        ),
    ]
