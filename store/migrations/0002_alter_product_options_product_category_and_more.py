# Generated by Django 5.0 on 2024-01-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Bracelets', max_length=30, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='store/blog', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='Stones', max_length=30, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='store/products', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(default='Stone Mix', max_length=30, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
