# Generated by Django 3.2.6 on 2021-10-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_pricefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishingproducts',
            name='price_discounted',
            field=models.IntegerField(null=True, verbose_name='قیمت با تخفیف'),
        ),
    ]
