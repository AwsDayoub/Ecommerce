# Generated by Django 4.2 on 2023-05-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_pho_user_status_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='pho',
            field=models.CharField(max_length=30),
        ),
    ]
