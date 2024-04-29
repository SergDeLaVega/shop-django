# Generated by Django 4.2.7 on 2024-04-23 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'verbose_name': 'Характеристики', 'verbose_name_plural': 'Характеристика'},
        ),
        migrations.AlterModelOptions(
            name='featurevalue',
            options={'verbose_name': 'Значение характеристики', 'verbose_name_plural': 'Значение характеристики'},
        ),
        migrations.AddField(
            model_name='products',
            name='feature_values',
            field=models.ManyToManyField(blank=True, to='goods.featurevalue', verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название характеристики'),
        ),
        migrations.AlterField(
            model_name='featurevalue',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Значение характеристики'),
        ),
        migrations.AlterField(
            model_name='products',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.feature', verbose_name='Характеристика'),
        ),
    ]
