# Generated by Django 4.2.7 on 2024-04-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_сonditionsitemcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='features',
            field=models.TextField(blank=True, verbose_name='Особенности'),
        ),
        migrations.AlterField(
            model_name='products',
            name='full_description',
            field=models.TextField(blank=True, verbose_name='Полное описание'),
        ),
    ]