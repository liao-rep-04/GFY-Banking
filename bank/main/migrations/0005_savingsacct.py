# Generated by Django 2.2.7 on 2019-12-02 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191202_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='savingsAcct',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13, null=True)),
                ('description', models.CharField(max_length=250)),
                ('transaction_date', models.DateField(null=True)),
                ('type_category', models.CharField(default='unknown', max_length=100, null=True)),
                ('transaction_type', models.CharField(default='transfer', max_length=100, null=True)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Accounts')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customers_List')),
            ],
        ),
    ]
