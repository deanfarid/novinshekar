# Generated by Django 3.2.6 on 2021-12-02 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20211201_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
