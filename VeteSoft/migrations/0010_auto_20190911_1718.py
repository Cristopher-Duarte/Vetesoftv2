# Generated by Django 2.1 on 2019-09-11 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0009_auto_20190911_1716'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='CentroVeterinario',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Examen',
        ),
        migrations.DeleteModel(
            name='Medicamento',
        ),
        migrations.DeleteModel(
            name='Medico',
        ),
        migrations.DeleteModel(
            name='Raza',
        ),
    ]
