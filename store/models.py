from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='store/blog')
    tag = models.CharField(max_length=30, default='Stones')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-pub_date']


class Product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='store/products')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    tag = models.CharField(max_length=30, default='Stone Mix')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
