# Generated by Django 4.2.6 on 2024-04-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_brand_image_alter_electric_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='', upload_to='cimg'),
        ),
        migrations.AlterField(
            model_name='electric_product',
            name='image',
            field=models.ImageField(blank=True, upload_to='cimg'),
        ),
    ]
