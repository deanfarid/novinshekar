# Generated by Django 3.2.6 on 2021-11-17 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cartitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]
