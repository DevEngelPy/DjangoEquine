# Generated by Django 5.0.7 on 2024-07-28 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Note_Sale', '0002_alter_note_previous_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='amount',
            field=models.FloatField(default=0, max_length=6, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='note',
            name='total',
            field=models.FloatField(default=0, max_length=6, verbose_name='total'),
        ),
    ]
