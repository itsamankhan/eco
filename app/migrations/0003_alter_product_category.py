# Generated by Django 5.0.7 on 2025-02-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_category_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('MW', 'Male Wear'), ('FW', 'Female Wear'), ('S', 'Sunglasses')], max_length=2, null=True),
        ),
    ]
