# Generated by Django 4.2 on 2023-06-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_customer_nees_contact_customer_need'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='postcode',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
