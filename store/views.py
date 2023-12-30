from django.shortcuts import render
from .models import Blog, Product


def home(request):
    return render(request, 'store/home.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'store/blog.html', {'blogs': blogs})


def product(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


def about(request):
    return render(request, 'store/about.html')
