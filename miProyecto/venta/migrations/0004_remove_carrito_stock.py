# Generated by Django 4.2.1 on 2023-07-05 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_carrito_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='stock',
        ),
    ]
