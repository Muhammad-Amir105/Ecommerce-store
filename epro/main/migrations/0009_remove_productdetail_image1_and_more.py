# Generated by Django 4.2.6 on 2024-05-02 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_productdetail_delete_product_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='image4',
        ),
        migrations.CreateModel(
            name='product_galary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='cimg')),
                ('elect_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.electric_product')),
            ],
        ),
    ]
