# Generated by Django 3.0.6 on 2020-10-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201002_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='name',
        ),
    ]
