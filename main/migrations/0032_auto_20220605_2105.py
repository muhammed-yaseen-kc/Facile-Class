# Generated by Django 3.2.8 on 2022-06-05 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20220605_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 21, 5, 12, 452863)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 21, 5, 12, 453862)),
        ),
    ]