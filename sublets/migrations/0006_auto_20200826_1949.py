# Generated by Django 3.1 on 2020-08-26 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0005_auto_20200825_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtenant',
            name='gr_address',
            field=models.CharField(default='N/A', max_length=1000),
        ),
        migrations.AddField(
            model_name='subtenant',
            name='gr_email',
            field=models.CharField(default='N/A', max_length=800),
        ),
        migrations.AddField(
            model_name='subtenant',
            name='gr_phone',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]