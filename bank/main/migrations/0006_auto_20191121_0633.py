# Generated by Django 2.2.7 on 2019-11-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191121_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=13),
        ),
    ]