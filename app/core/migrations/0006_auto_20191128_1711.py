# Generated by Django 2.2.7 on 2019-11-28 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191128_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='price_field',
            new_name='price',
        ),
    ]
