# Generated by Django 3.2.7 on 2021-09-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0010_orderitem_itemamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='eatingType',
            field=models.CharField(choices=[('DineIn', 'DineIn'), ('TakeAway', 'TakeAway')], default='DineIn', max_length=20),
        ),
    ]
