# Generated by Django 3.2.8 on 2022-04-10 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20220410_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 20, 49, 44, 585327)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 20, 49, 44, 586328)),
        ),
    ]
