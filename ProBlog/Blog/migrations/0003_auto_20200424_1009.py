# Generated by Django 3.0.3 on 2020-04-24 08:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20200424_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 24, 8, 9, 47, 481349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 8, 9, 47, 479354, tzinfo=utc)),
        ),
    ]