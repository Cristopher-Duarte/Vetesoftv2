# Generated by Django 2.1 on 2019-09-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0003_auto_20190919_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examenmascota',
            name='Examen',
        ),
        migrations.AddField(
            model_name='examenmascota',
            name='TipoExamen',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Examen',
        ),
    ]
