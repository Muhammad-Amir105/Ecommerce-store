# Generated by Django 4.2.6 on 2024-05-02 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_elect_product_product_galary_electproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='category',
        ),
    ]
