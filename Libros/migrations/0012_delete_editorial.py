# Generated by Django 5.1.3 on 2024-11-18 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0011_alter_libro_tipo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editorial',
        ),
    ]
