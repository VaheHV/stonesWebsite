# Generated by Django 5.0 on 2024-01-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bracelets', 'Ձեռնաշղթաներ'), ('rings', 'Մատանիներ'), ('earrings', 'Ականջօղներ'), ('necklaces', 'Վզնոցներ'), ('colognes', 'Կուլոններ'), ('other', 'Այլ')], default='other', max_length=20, verbose_name='Категория'),
        ),
    ]
