# Generated by Django 2.1 on 2019-09-13 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0014_auto_20190913_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='Genero',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Genero'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='Genero',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Genero'),
        ),
    ]
