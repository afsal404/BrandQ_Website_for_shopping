# Generated by Django 4.2.11 on 2024-05-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0014_alter_cart_data_p_image_alter_cart_data_p_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_data',
            name='Useremail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
