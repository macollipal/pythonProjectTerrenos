# Generated by Django 3.2.2 on 2021-06-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210616_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eval_terrenos',
            name='fecha_ini_diseno_ter',
            field=models.DateField(null=True, verbose_name='Fecha Inicio Diseño'),
        ),
    ]