# Generated by Django 2.1 on 2019-09-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0011_auto_20190911_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='Estado',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='FechaRegistro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Estado',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='FechaRegistro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='Estado',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='FechaRegistro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
