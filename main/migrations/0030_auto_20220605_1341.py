# Generated by Django 3.2.8 on 2022-06-05 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20220605_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 13, 41, 39, 378909)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 13, 41, 39, 378909)),
        ),
    ]
