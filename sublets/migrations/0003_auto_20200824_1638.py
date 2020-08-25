# Generated by Django 3.1 on 2020-08-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0002_subtenant_chosen_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtenant',
            name='payment_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='sublet_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subletlisting',
            name='sublet_start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subtenant',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
