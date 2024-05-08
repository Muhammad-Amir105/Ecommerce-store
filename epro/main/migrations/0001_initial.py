# Generated by Django 4.2.6 on 2024-04-30 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='main/cimg')),
                ('description', models.CharField(max_length=200)),
                ('is_populer', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='main/cimg')),
                ('description', models.CharField(max_length=200)),
                ('orignal_price', models.CharField(max_length=50)),
                ('discount', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catagory')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catagory'),
        ),
    ]
