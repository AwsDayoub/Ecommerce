# Generated by Django 4.1.7 on 2023-07-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='D:\\Ecom\\Ecom\\static\\images\\images'),
        ),
    ]
