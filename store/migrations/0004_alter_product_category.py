# Generated by Django 5.0 on 2024-01-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_blog_options_alter_blog_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bracelets', 'Ձեռնաշղթաներ'), ('necklaces', 'Մատանիներ'), ('earrings', 'Ականջօղներ'), ('rings', 'Վզնոցներ'), ('colognes', 'Կուլոններ'), ('other', 'Այլ')], default='other', max_length=20, verbose_name='Категория'),
        ),
    ]
