# Generated by Django 3.1 on 2020-08-25 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sublets', '0004_auto_20200825_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtenant',
            name='chosen_sub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sublets.subletlisting'),
        ),
    ]
