# Generated by Django 3.1 on 2020-08-27 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0008_subletplace_landlord'),
    ]

    operations = [
        migrations.AddField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 18, 59, 27, 222548)),
        ),
        migrations.AddField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 18, 59, 27, 222548)),
        ),
    ]
