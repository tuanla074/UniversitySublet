# Generated by Django 3.1 on 2020-08-30 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0021_auto_20200830_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 19, 25, 28, 916467)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 19, 25, 28, 916467)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='sublet_main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
