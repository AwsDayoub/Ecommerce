# Generated by Django 4.2 on 2023-06-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/default-placeholder.png', null=True, upload_to=''),
        ),
    ]