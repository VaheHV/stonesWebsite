from django.shortcuts import render
from .models import Blog, Product


def home(request):
    blogs = Blog.objects.all()[:4]
    return render(request, 'store/home.html', {'blogs': blogs})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'store/blog.html', {'blogs': blogs})


def products(request):
    products_all = Product.objects.all()
    return render(request, 'store/products.html', {'products': products_all})


def about(request):
    return render(request, 'store/about.html')


def article_page(request, pk):
    article = Blog.objects.get(id=pk)
    return render(request, 'store/article.html', {'article': article})


def product_page(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product_page.html', {'product': product})
