# Generated by Django 3.1 on 2020-08-28 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0010_auto_20200827_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 13, 28, 41, 404148)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 13, 28, 41, 404148)),
        ),
    ]