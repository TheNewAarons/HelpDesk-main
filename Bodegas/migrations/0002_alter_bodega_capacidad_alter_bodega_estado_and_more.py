# Generated by Django 5.1.3 on 2024-11-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bodegas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='capacidad',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='estado',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='nivel_stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='tamaño_bodega',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
