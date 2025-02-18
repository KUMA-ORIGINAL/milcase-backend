# Generated by Django 5.1 on 2025-02-18 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_favorite'),
        ('products', '0006_alter_category_options_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
