# Generated by Django 5.0.7 on 2024-08-08 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_product_model_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='model_type',
            new_name='product_type',
        ),
    ]
