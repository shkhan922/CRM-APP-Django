# Generated by Django 3.0.6 on 2020-10-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201002_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='customer_name',
        ),
    ]
