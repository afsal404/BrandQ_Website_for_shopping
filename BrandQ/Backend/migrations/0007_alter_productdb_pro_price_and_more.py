# Generated by Django 4.2.11 on 2024-04-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_auto_20231122_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='pro_price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productdb',
            name='pro_product_imagee',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='productdb',
            name='pro_product_imageee',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
