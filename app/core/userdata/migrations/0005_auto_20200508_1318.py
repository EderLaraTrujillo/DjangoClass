# Generated by Django 2.2.12 on 2020-05-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_auto_20200508_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='pcrHabil',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
