# Generated by Django 5.0.7 on 2024-07-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_rename_account_credit_client_abono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='abono',
            field=models.FloatField(default=0, verbose_name='abono'),
        ),
    ]
