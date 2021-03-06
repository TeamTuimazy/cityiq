# Generated by Django 3.1.2 on 2020-11-28 12:54

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201128_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexiq',
            name='direction1',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Городское управление'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction10',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Экономическое состояние и инвестиционный климат'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction2',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Инновации для городской среды'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction3',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Интеллектуальные системы общественной безопасности'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction4',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Инфраструктура сетей связи'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction5',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Умное ЖКХ'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction6',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Умный городской транспорт'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction7',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Интеллектуальные системы экологической безопасности'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='direction9',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Интеллектуальные системы социальных услуг'),
        ),
        migrations.AlterField(
            model_name='indexiq',
            name='index_iq',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=5, verbose_name='Итоговый индекс IQ'),
        ),
    ]
