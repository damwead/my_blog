# Generated by Django 3.1.7 on 2021-03-19 18:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210319_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 19, 18, 40, 35, 622460, tzinfo=utc)),
        ),
    ]
