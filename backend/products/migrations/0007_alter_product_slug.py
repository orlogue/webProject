# Generated by Django 4.0.4 on 2022-05-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
