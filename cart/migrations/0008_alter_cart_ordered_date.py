# Generated by Django 3.2.6 on 2021-12-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='ordered_date',
            field=models.DateTimeField(null=True, verbose_name='زمان تحویل'),
        ),
    ]
