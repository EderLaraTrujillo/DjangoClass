# Generated by Django 2.2.12 on 2020-05-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200507_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='apelUser',
            field=models.CharField(max_length=200, null=True, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='geneUser',
            field=models.CharField(choices=[('Femenino', 'F'), ('Masculino', 'M'), ('Otro', 'Otro')], default='Otro', max_length=20, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='nombUser',
            field=models.CharField(max_length=200, null=True, verbose_name='Nombres'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='profeUser',
            field=models.CharField(max_length=100, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='teleUser',
            field=models.CharField(max_length=20, verbose_name='Número de Teléfono'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='userDNI',
            field=models.CharField(max_length=20, verbose_name='Identificación'),
        ),
    ]
