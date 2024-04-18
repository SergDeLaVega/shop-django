# Generated by Django 4.2.7 on 2024-04-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название секции')),
            ],
            options={
                'verbose_name': 'Самое покупаемое',
                'verbose_name_plural': 'Самое покупаемое',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название секции')),
            ],
            options={
                'verbose_name': 'Новинки',
                'verbose_name_plural': 'Новинки',
            },
        ),
    ]
