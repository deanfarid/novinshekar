# Generated by Django 3.2.6 on 2021-12-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_profilemodel_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='home',
            field=models.BigIntegerField(null=True, unique=True, verbose_name='تلفن ثابت '),
        ),
    ]
