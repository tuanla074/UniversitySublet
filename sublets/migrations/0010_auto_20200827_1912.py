# Generated by Django 3.1 on 2020-08-27 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0009_auto_20200827_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 19, 12, 55, 363988)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 19, 12, 55, 363988)),
        ),
    ]
