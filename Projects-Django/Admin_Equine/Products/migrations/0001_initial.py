# Generated by Django 5.0.7 on 2024-07-27 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Product_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.FloatField(max_length=6, verbose_name='price')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.type', verbose_name='type')),
            ],
            options={
                'verbose_name': 'Product_shop',
                'verbose_name_plural': 'Product_shops',
            },
        ),
        migrations.CreateModel(
            name='Product_sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.FloatField(max_length=6, verbose_name='price')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.type', verbose_name='type')),
            ],
            options={
                'verbose_name': 'Product_sale',
                'verbose_name_plural': 'Product_sales',
            },
        ),
    ]
