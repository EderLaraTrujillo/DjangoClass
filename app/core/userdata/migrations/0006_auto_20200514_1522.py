# Generated by Django 2.2.12 on 2020-05-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_auto_20200508_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUser',
            field=models.ImageField(default='user.png', upload_to='perfiles/img', verbose_name='Foto de perfil'),
        ),
    ]
