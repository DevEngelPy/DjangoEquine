# Generated by Django 5.0.7 on 2024-07-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kitchen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cooked_equino',
            name='id_product_reguistration',
        ),
        migrations.AddField(
            model_name='cooked_equino',
            name='product',
            field=models.CharField(choices=[('TRE', 'Tripa Equino')], default='TRE', max_length=50, verbose_name='product'),
        ),
    ]
