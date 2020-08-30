# Generated by Django 3.1 on 2020-08-30 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0017_auto_20200830_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 18, 54, 21, 101484)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 30, 18, 54, 21, 101484)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='sublet_main_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]