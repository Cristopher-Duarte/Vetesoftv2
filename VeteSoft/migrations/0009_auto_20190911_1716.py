# Generated by Django 2.1 on 2019-09-11 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0008_auto_20190911_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citas',
            name='Mascotas',
        ),
        migrations.RemoveField(
            model_name='citas',
            name='Medico',
        ),
        migrations.RemoveField(
            model_name='detallecita',
            name='Citas',
        ),
        migrations.RemoveField(
            model_name='detallecita',
            name='ExamenMascota',
        ),
        migrations.RemoveField(
            model_name='detallecita',
            name='Medicamento',
        ),
        migrations.RemoveField(
            model_name='examenmascota',
            name='Examen',
        ),
        migrations.RemoveField(
            model_name='mascotas',
            name='Cliente',
        ),
        migrations.RemoveField(
            model_name='mascotas',
            name='HistoriaCliente',
        ),
        migrations.RemoveField(
            model_name='mascotas',
            name='Raza',
        ),
        migrations.RemoveField(
            model_name='resultadoclinico',
            name='ExamenMascota',
        ),
        migrations.DeleteModel(
            name='Citas',
        ),
        migrations.DeleteModel(
            name='DetalleCita',
        ),
        migrations.DeleteModel(
            name='ExamenMascota',
        ),
        migrations.DeleteModel(
            name='HistoriaCliente',
        ),
        migrations.DeleteModel(
            name='Mascotas',
        ),
        migrations.DeleteModel(
            name='ResultadoClinico',
        ),
    ]
