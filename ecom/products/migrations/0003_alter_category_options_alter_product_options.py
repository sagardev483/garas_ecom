# Generated by Django 5.1.7 on 2025-04-26 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'ordering': ['name'], 'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'ordering': ['-date_added'], 'verbose_name': 'Product'},
        ),
    ]
