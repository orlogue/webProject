# Generated by Django 4.0.4 on 2022-07-07 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_telegram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegram',
            old_name='user_id',
            new_name='user',
        ),
    ]
