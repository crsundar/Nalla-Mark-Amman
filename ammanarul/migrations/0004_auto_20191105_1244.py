# Generated by Django 2.2.6 on 2019-11-05 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ammanarul', '0003_auto_20191104_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='display_upto',
            field=models.DateField(default=datetime.date(2019, 12, 3)),
        ),
    ]