# Generated by Django 4.0.4 on 2022-05-29 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='duracion',
            new_name='conformacion',
        ),
    ]
