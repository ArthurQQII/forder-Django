# Generated by Django 3.2.7 on 2021-09-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0006_auto_20210922_1144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderItem',
        ),
    ]
