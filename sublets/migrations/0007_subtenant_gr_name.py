# Generated by Django 3.1 on 2020-08-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0006_auto_20200826_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtenant',
            name='gr_name',
            field=models.CharField(default='N/A', max_length=500),
        ),
    ]
