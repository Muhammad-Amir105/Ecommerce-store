# Generated by Django 4.2.6 on 2024-05-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_brand_image_alter_electric_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, upload_to='cimg')),
                ('image2', models.ImageField(blank=True, upload_to='cimg')),
                ('image3', models.ImageField(blank=True, upload_to='cimg')),
                ('image4', models.ImageField(blank=True, upload_to='cimg')),
                ('about_image', models.ImageField(blank=True, upload_to='cimg')),
                ('about_title', models.CharField(max_length=50)),
                ('about_discription', models.CharField(max_length=200)),
                ('tech_image', models.ImageField(blank=True, upload_to='cimg')),
                ('tech_title', models.CharField(max_length=50)),
                ('tech_discription', models.CharField(max_length=200)),
                ('camera_image', models.ImageField(blank=True, upload_to='cimg')),
                ('camera_title', models.CharField(max_length=50)),
                ('camera_discription', models.CharField(max_length=200)),
                ('technlogy_image', models.ImageField(blank=True, upload_to='cimg')),
                ('technlogy_title', models.CharField(max_length=50)),
                ('technlogy_discription', models.CharField(max_length=200)),
                ('design_image', models.ImageField(blank=True, upload_to='cimg')),
                ('design_title', models.CharField(max_length=50)),
                ('design_discription', models.CharField(max_length=200)),
            ],
        ),
    ]
