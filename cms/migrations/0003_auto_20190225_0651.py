# Generated by Django 2.1.5 on 2019-02-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20190224_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='severity',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
    ]
