# Generated by Django 3.2.6 on 2021-11-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_keyval_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishingproducts',
            name='image',
            field=models.ManyToManyField(related_name='image', to='products.Images', verbose_name='عکس ها'),
        ),
    ]
