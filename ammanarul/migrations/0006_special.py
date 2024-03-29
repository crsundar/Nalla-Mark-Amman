# Generated by Django 2.2.6 on 2019-11-06 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ammanarul', '0005_auto_20191106_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('prayer', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_on', models.DateField(default=datetime.date.today)),
                ('display_upto', models.DateField(default=datetime.date(2019, 12, 4))),
                ('profile', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
