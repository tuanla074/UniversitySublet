# Generated by Django 3.1 on 2020-08-29 16:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0014_auto_20200828_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sublets.subletlisting'),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='end_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 12, 33, 55, 932210)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='start_date_search',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 12, 33, 55, 932210)),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='sublet_main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
