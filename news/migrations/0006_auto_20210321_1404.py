# Generated by Django 3.1.7 on 2021-03-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210319_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
