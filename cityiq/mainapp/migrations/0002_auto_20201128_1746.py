# Generated by Django 3.1.2 on 2020-11-28 12:46

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='dst',
        ),
        migrations.RemoveField(
            model_name='message',
            name='src',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='event',
        ),
        migrations.RemoveField(
            model_name='task',
            name='executor',
        ),
        migrations.RemoveField(
            model_name='historyindexiq',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator11',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator12',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator13',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator14',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator15',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator16',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator17',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator18',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator19',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator20',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator21',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator22',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator23',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator24',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator25',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator26',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator27',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator28',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator29',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator30',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator31',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator32',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator33',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator34',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator35',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator36',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator37',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator38',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator39',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator40',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator41',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator42',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator43',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator44',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator45',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator46',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='indicator47',
        ),
        migrations.RemoveField(
            model_name='indexiq',
            name='owner',
        ),
        migrations.AddField(
            model_name='indexiq',
            name='direction8',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=5, verbose_name='Туризм и сервис'),
        ),
        migrations.AlterField(
            model_name='city',
            name='qty_peopls',
            field=models.IntegerField(blank=True, default=0, verbose_name='Население'),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
