# Generated by Django 4.1.7 on 2023-07-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]