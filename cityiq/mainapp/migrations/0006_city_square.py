# Generated by Django 3.1.2 on 2020-11-28 20:20

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201128_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='square',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=10, verbose_name='Площадь'),
        ),
    ]
