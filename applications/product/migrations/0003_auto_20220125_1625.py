# Generated by Django 3.2.10 on 2022-01-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='woman',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='man',
            field=models.BooleanField(default=True),
        ),
    ]
