# Generated by Django 3.2.7 on 2021-09-12 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210912_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 12, 7, 37, 198944)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 12, 7, 37, 198944)),
        ),
    ]
