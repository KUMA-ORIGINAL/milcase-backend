# Generated by Django 5.1 on 2025-02-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True, blank=True, verbose_name='День рождения'),
            preserve_default=False,
        ),
    ]
