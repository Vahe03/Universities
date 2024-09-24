# Generated by Django 4.0.4 on 2022-04-23 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_university_created_at_university_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 58, 18, 806025, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 58, 18, 806367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='university',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 58, 18, 806025, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='university',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 58, 18, 806367, tzinfo=utc)),
        ),
    ]
