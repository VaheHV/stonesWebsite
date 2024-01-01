from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='store/blog', verbose_name='Изображение')
    tag = models.CharField(max_length=30, default='քարեր', verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-pub_date']


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='store/products', verbose_name='Изображение')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, verbose_name='Цена')
    CATEGORY_CHOICES = [
        ('bracelets', 'Բրասլետներ'),
        ('rings', 'Մատանիներ'),
        ('earrings', 'Ականջօղներ'),
        ('necklaces', 'Վզնոցներ'),
        ('colognes', 'Կուլոններ'),
        ('other', 'Այլ')
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name='Категория')
    tag = models.CharField(max_length=30, default='քարեր', verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
