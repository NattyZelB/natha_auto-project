# Generated by Django 4.2 on 2023-06-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Automatisch', 'Automatisch'), ('Manueel', 'Manueel'), ('Halve transmissie', 'Halve transmissie')], max_length=100),
        ),
    ]
