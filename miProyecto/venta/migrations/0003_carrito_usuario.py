# Generated by Django 4.2.1 on 2023-07-05 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
