# Generated by Django 4.0.1 on 2022-01-16 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='blog.relatedblog'),
        ),
    ]