# Generated by Django 4.0.4 on 2022-05-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_building_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='building',
            field=models.CharField(max_length=30),
        ),
    ]