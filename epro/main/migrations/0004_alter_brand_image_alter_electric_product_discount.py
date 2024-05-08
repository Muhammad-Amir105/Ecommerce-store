# Generated by Django 4.2.6 on 2024-04-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_product_electric_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='', upload_to='main/cimg'),
        ),
        migrations.AlterField(
            model_name='electric_product',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
