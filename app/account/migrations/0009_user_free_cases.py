# Generated by Django 5.1 on 2025-02-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_favorite_products_delete_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='free_cases',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество бесплатных чехлов'),
        ),
    ]
