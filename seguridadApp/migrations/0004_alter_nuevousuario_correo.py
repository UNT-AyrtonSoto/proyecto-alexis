# Generated by Django 4.0.5 on 2022-08-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridadApp', '0003_alter_nuevousuario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuevousuario',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
    ]