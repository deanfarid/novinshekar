# Generated by Django 3.2.6 on 2021-12-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profilemodel_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
    ]