# Generated by Django 3.2.8 on 2022-10-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_like_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]