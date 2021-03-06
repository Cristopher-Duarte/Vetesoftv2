# Generated by Django 2.1 on 2019-09-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0002_delete_administrador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Documento', models.CharField(max_length=45)),
                ('Nombres', models.CharField(max_length=45)),
                ('PrimerApellido', models.CharField(max_length=45)),
                ('SegundoApellido', models.CharField(max_length=45)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(max_length=45)),
                ('Celular', models.CharField(max_length=45)),
                ('Direccion', models.CharField(max_length=45)),
                ('FechaRegistro', models.DateField()),
                ('Estado', models.BooleanField(null=True)),
            ],
        ),
    ]
