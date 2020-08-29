# Generated by Django 3.1 on 2020-08-28 19:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0013_auto_20200828_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='image',
        ),
        migrations.AddField(
            model_name='subletlisting',
            name='sublet_main_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sublets.imagemodel'),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 15, 39, 28, 339007)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 28, 15, 39, 28, 339007)),
        ),
    ]
