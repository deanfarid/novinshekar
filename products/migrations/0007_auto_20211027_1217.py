# Generated by Django 3.2.6 on 2021-10-27 08:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_fishingproducts_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fishingproducts',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AddField(
            model_name='fishingproducts',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL, verbose_name='دیس لایک'),
        ),
    ]
